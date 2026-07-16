from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.config import settings
from backend.constants import SUPPORT_EMAIL
from backend.models import ChatRequest

from backend.services.classifier_service import (
    classify_question,
    wants_human_support,
    wants_unavailable_action,
    detects_misuse,
)
from backend.services.search_service import search_knowledge_base
from backend.services.ai_service import generate_response
from backend.services.web_search_service import search_web
from backend.services.session_service import (
    add_message,
    get_session,
    clear_session
)
from backend.services.logger_service import log_chat_event
from backend.services.escalation_service import flag_misuse

from backend.utils.validators import validate_chat_request

from backend.routes import upload
from backend.routes import feedback
from backend.routes import escalate
from backend.routes import health
from backend.routes import chat as chat_routes
from backend.routes import admin


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(feedback.router, prefix="/feedback", tags=["Feedback"])
app.include_router(escalate.router, prefix="/escalate", tags=["Escalation"])
app.include_router(health.router, prefix="/route-health", tags=["Health"])
app.include_router(chat_routes.router, prefix="/route-chat", tags=["Chat"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])


# --------------------------------------------------------------------------
# Minimal per-session cache of the last successful KB result.
# This lets low-signal follow-ups ("still stuck") re-use the previous
# diagnosis's source content instead of triggering a fresh, unfocused
# search that has nothing real to match against.
#
# NOTE: this is in-memory and will reset on backend restart / won't work
# across multiple backend instances. If you already track per-session
# state in session_service.py, move this dict (or equivalent) there so
# it persists/scales the same way session history does.
# --------------------------------------------------------------------------
_last_kb_result_by_session: dict[str, dict] = {}


@app.get("/")
def root():
    return {
        "message": "Brainy API is running",
        "version": settings.APP_VERSION
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/version")
def version():
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    validation = validate_chat_request(request.user_message)

    if not validation["valid"]:
        return {
            "error": validation["error"],
            "session_id": request.session_id
        }

    session_id = request.session_id or "default"

    lab_context = {
        "lab_id": request.lab_id,
        "lab_name": request.lab_name,
        "exercise": request.exercise,
        "task": request.task,
        "step": request.step
    }

    add_message(session_id, "user", request.user_message)

    question_type = classify_question(request.user_message)

    # Only treat lab context fields as genuinely unset when NO workshop has
    # been selected at all. The sidebar starts with generic placeholder text
    # ("current-lab" / "Current CloudLabs Lab" / "Exercise 1" / "Task 1" /
    # "Step 1") before the learner picks a workshop, so a plain empty-string/
    # None check isn't enough there. BUT once the learner has actually
    # selected a real workshop from the "Workshop / Lab Guide" dropdown
    # (lab_id is no longer the "current-lab" fallback), the Exercise/Task/
    # Step fields shown in the sidebar ARE the learner's real, currently
    # selected context -- even if they still read the defaults "Exercise 1"/
    # "Task 1"/"Step 1" (a perfectly common, real starting point) -- and
    # must be trusted as-is instead of being discarded as guesswork. Previously
    # they were always nulled out on a literal string match, so Brainy kept
    # asking "which lab/exercise are you on?" even though it was clearly
    # selected in the UI. Computed up front (before the KB search) so
    # lab_id/exercise/task/step are ALWAYS applied together as structured
    # search metadata, not just used later in the prompt text.
    PLACEHOLDER_LAB_CONTEXT = {
        "lab_id": "current-lab",
        "lab_name": "current cloudlabs lab",
        "exercise": "exercise 1",
        "task": "task 1",
        "step": "step 1",
    }

    lab_selected = bool(request.lab_id) and (
        request.lab_id.strip().lower() != PLACEHOLDER_LAB_CONTEXT["lab_id"]
    )

    def _real_value(field: str, value: str | None) -> str | None:
        if not value:
            return None
        if field in ("exercise", "task", "step") and lab_selected:
            return value
        if value.strip().lower() == PLACEHOLDER_LAB_CONTEXT[field]:
            return None
        return value

    real_lab_name = _real_value("lab_name", request.lab_name)
    real_exercise = _real_value("exercise", request.exercise)
    real_task = _real_value("task", request.task)
    real_step = _real_value("step", request.step)

    # Detected straight from the learner's own message (e.g. "connect me to
    # support", "talk to a human") -- independent of question_type/AI wording,
    # so an explicit ask for a human is never missed.
    user_requested_support = wants_human_support(request.user_message)

    # Detected straight from the learner's own message too: are they asking
    # Brainy to actually PERFORM an account/environment action (e.g. "can
    # you extend lab duration?") rather than asking for information? Brainy
    # has no real access to do these, so this always routes to support
    # instead of letting the AI guess or ask an unhelpful clarifying
    # question about which platform/lab -- the answer is the same either way.
    requests_unavailable_action = wants_unavailable_action(request.user_message)

    # Detected straight from the learner's own message: does it look like
    # an attempt to misuse the lab environment (spin up extra/unauthorized
    # resources, bypass quotas, crypto-mine) or something clearly malicious
    # (jailbreak/prompt-injection attempts, credential theft, attacking
    # other systems)? Brainy must never try to help with these -- it should
    # refuse and the session gets auto-flagged for the CloudLabs
    # support/proctor team to review (see GET /admin/alerts).
    attempts_misuse = detects_misuse(request.user_message)

    if attempts_misuse:
        flag_misuse(
            session_id=session_id,
            user_message=request.user_message,
            reason="Possible lab misuse or policy violation detected",
            lab_context=lab_context,
        )

    # Casual chit-chat (greetings/thanks/acknowledgements) shouldn't touch
    # the knowledge base at all, and must NEVER reuse a previous session's
    # cached KB result -- that produced replies like "hi" coming back with
    # an unrelated login-issues.md source from an earlier question.
    if question_type == "greeting":
        kb_result = {
            "found": False,
            "source": None,
            "content": "",
            "score": 0,
            "low_signal": True,
        }
    else:
        # IMPORTANT: search on the learner's RAW message only. Do not wrap it
        # in the "Lab Name: / Exercise: / Task: / Step:" template before
        # searching -- those literal labels used to pollute keyword scoring
        # on every single request. Structured lab/exercise/task/step context
        # is passed separately below so it's used as metadata matching
        # instead of noisy free-text -- ALL FOUR fields are always passed
        # together so the retrieved content is scoped to the learner's exact
        # exercise and step, not just the lab/task.
        kb_result = search_knowledge_base(
            request.user_message,
            question_type,
            request.lab_id,
            real_exercise,
            real_task,
            real_step,
        )

        # If this message didn't carry enough real signal (e.g. a generic
        # "still stuck" follow-up) AND we couldn't resolve it to the current
        # step's content either, fall back to the last successful KB result
        # for this session instead of trusting a near-empty/unfocused search.
        # A "context_only" lookup (see search_service) already found real
        # content for the learner's current exercise/task/step, so it must
        # NOT be discarded in favor of a stale previous answer.
        if (
            kb_result.get("low_signal")
            and not kb_result.get("found")
            and session_id in _last_kb_result_by_session
        ):
            kb_result = _last_kb_result_by_session[session_id]
        elif kb_result.get("found"):
            _last_kb_result_by_session[session_id] = kb_result

        # A context-only lookup means the learner hasn't described an actual
        # problem yet -- the retrieved content is just the current step's
        # instructions, not a matched diagnosis. Flag this clearly for the
        # AI so it asks a specific, grounded clarifying question about why
        # the learner can't complete that step, instead of either a fully
        # generic question or jumping straight to troubleshooting steps.
        if kb_result.get("context_only"):
            kb_result = {
                **kb_result,
                "content": (
                    "NOTE: The learner has not described a specific problem "
                    "yet. The content below is simply the official lab "
                    "guide's instructions for the exercise/task/step they "
                    "are currently on (not a matched diagnosis). Briefly "
                    "reference what this step actually asks them to do, "
                    "then ask a short, specific question about what's "
                    "happening when they try it or why they're unable to "
                    "complete it (e.g. an error message, nothing happening, "
                    "an unexpected result, or not knowing where to click). "
                    "Do not give troubleshooting steps yet -- no problem "
                    "has been described.\n\n" + kb_result["content"]
                ),
            }

    history = get_session(session_id)

    # If the knowledge base has no strong match for a real lab/troubleshooting
    # question, fall back to a best-effort general web search so the learner
    # still gets useful guidance instead of a dead end. Never blocks/breaks
    # the chat response if the search fails -- search_web() always returns
    # a plain list, empty on any error.
    web_results = []

    if (
        question_type in ("troubleshooting", "lab_help")
        and not kb_result.get("found")
        and not kb_result.get("low_signal")
    ):
        web_results = search_web(request.user_message)

    context_lines = [
        f"Lab Name: {real_lab_name}" if real_lab_name else None,
        f"Exercise: {real_exercise}" if real_exercise else None,
        f"Task: {real_task}" if real_task else None,
        f"Step: {real_step}" if real_step else None,
    ]
    context_lines = [line for line in context_lines if line]

    lab_context_section = (
        "Current Lab Context:\n" + "\n".join(context_lines)
        if context_lines
        else "Current Lab Context: Not provided -- do not assume any "
        "specific exercise, task, or step. This does NOT mean you should "
        "withhold help: if the learner describes an actual problem (an "
        "error, something not working, being stuck) and the knowledge base "
        "content above has relevant troubleshooting guidance, give that "
        "guidance directly right away using the general/common steps -- do "
        "not block a real troubleshooting answer on first asking which lab "
        "or exercise they're in. Only ask which lab/exercise they need help "
        "with if the retrieved knowledge base content isn't relevant or the "
        "answer genuinely depends on which lab/platform they're using."
    )

    ai_prompt = f"""
    {lab_context_section}

    User Question:
    {request.user_message}
    """

    if attempts_misuse:
        # Deterministic refusal -- never let the model see/respond to this
        # request, since it's a policy-violation signal, not a real
        # question to answer or clarify.
        ai_answer = (
            "I can't help with that -- it looks like it would misuse the "
            "lab environment or go against acceptable-use policy (e.g. "
            "provisioning extra/unauthorized resources or bypassing "
            "restrictions). I've flagged this for the CloudLabs support/"
            "proctor team to review. "
            f"If you believe this is a mistake, please reach out to CloudLabs "
            f"Support at {SUPPORT_EMAIL}."
        )
    elif requests_unavailable_action:
        # Deterministic, not model-generated: this is an action Brainy
        # genuinely cannot perform regardless of which lab/platform is
        # involved, so skip the AI call entirely rather than risk it
        # hallucinating a workaround or asking a pointless clarifying
        # question.
        ai_answer = (
            "I'm an AI lab copilot, so I don't have the ability to make "
            "account or environment changes myself -- things like "
            "extending lab duration, unlocking access, issuing refunds, "
            "or changing a subscription. "
            f"Please reach out to CloudLabs Support at {SUPPORT_EMAIL} and "
            "they'll be able to help with this directly."
        )
    else:
        ai_answer = generate_response(
            ai_prompt,
            kb_result["content"],
            history,
            casual=(question_type == "greeting"),
            web_results=web_results,
        )

    # Deterministic safety net: if this was a real lab/troubleshooting
    # question (not a low-signal follow-up) and neither the knowledge base
    # nor a web search fallback turned up anything, OR the model's own
    # answer already signals it can't actually help (defers to support/an
    # administrator, or says it lacks the ability/access to do something),
    # always make sure the actual CloudLabs support email address is
    # present -- don't rely on the model to remember to include it, since
    # it inconsistently says things like "point you to the right support
    # channel" or "I don't have the ability to do that" without ever
    # naming the address.
    no_answer_available = (
        question_type in ("troubleshooting", "lab_help")
        and not kb_result.get("found")
        and not kb_result.get("low_signal")
        and not web_results
    )

    NO_ANSWER_PHRASES = (
        "contact support",
        "reach out",
        "support team",
        "support channel",
        "support contact",
        "lab administrator",
        "cloudlabs support",
        "customer support",
        "point you to",
        "who to contact",
        "i don't have the ability",
        "i do not have the ability",
        "i'm not able to",
        "i am not able to",
        "i don't have access",
        "i do not have access",
        "outside my scope",
        # Broader refusal phrasings so unusual/out-of-scope demands (things
        # Brainy simply can't do, e.g. "book something", "connect me to
        # support directly", "delete my account") still deterministically
        # surface the support email even when the model's exact wording
        # doesn't match one of the narrower phrases above.
        "i can't do that",
        "i cannot do that",
        "i can't help with that",
        "i cannot help with that",
        "i can't assist with",
        "i cannot assist with",
        "i can't fulfill",
        "i cannot fulfill",
        "i can't connect you",
        "i cannot connect you",
        "i can't provide",
        "i cannot provide",
        "i'm unable to",
        "i am unable to",
        "not something i can",
        "not able to do that",
        "beyond my capabilities",
        "beyond what i can",
        "outside what i can",
        "i don't have the capability",
        "i do not have the capability",
        "i'm just an ai",
        "i am just an ai",
        "as an ai",
    )
    signals_no_answer = any(
        phrase in ai_answer.lower() for phrase in NO_ANSWER_PHRASES
    )

    if SUPPORT_EMAIL not in ai_answer and (
        user_requested_support
        or requests_unavailable_action
        or no_answer_available
        or signals_no_answer
    ):
        ai_answer = (
            ai_answer.rstrip()
            + f"\n\nYou can reach CloudLabs Support at {SUPPORT_EMAIL} for further assistance."
        )

    # Single, authoritative signal for the frontend to decide whether to
    # show the "Connect with Support" CTA -- combines an explicit learner
    # request, an unavailable-action ask, the deterministic no-answer case,
    # and the AI's own refusal wording, instead of the frontend having to
    # re-detect this by scanning the answer text for the support email.
    needs_support = (
        user_requested_support
        or requests_unavailable_action
        or no_answer_available
        or signals_no_answer
        or attempts_misuse
    )

    add_message(session_id, "assistant", ai_answer)

    log_chat_event(
        session_id=session_id,
        user_message=request.user_message,
        ai_answer=ai_answer,
        question_type=question_type,
        source=kb_result["source"],
        score=kb_result.get("score", 0),
        lab_context=lab_context,
        web_search_used=bool(web_results),
    )

    return {
        "session_id": session_id,
        "question_type": question_type,
        "answer": ai_answer,
        "source": kb_result["source"],
        "found": kb_result["found"],
        "score": kb_result.get("score", 0),
        "history": get_session(session_id),
        "lab_context": lab_context,
        "web_search_used": bool(web_results),
        "web_sources": web_results,
        "needs_support": needs_support,
    }


@app.delete("/session/{session_id}")
def delete_session(session_id: str):

    clear_session(session_id)

    if session_id in _last_kb_result_by_session:
        del _last_kb_result_by_session[session_id]

    return {
        "message": f"Session '{session_id}' cleared successfully."
    }
