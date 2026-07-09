from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.config import settings
from backend.models import ChatRequest

from backend.services.classifier_service import classify_question
from backend.services.search_service import search_knowledge_base
from backend.services.ai_service import generate_response
from backend.services.session_service import (
    add_message,
    get_session,
    clear_session
)
from backend.services.logger_service import log_chat_event

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
        # in the "Lab Name: / Task: / Step:" template before searching --
        # those literal labels used to pollute keyword scoring on every single
        # request. Structured lab/task/step context is passed separately below
        # so it can be used as metadata matching instead of noisy free-text.
        kb_result = search_knowledge_base(
            request.user_message,
            question_type,
            request.lab_id,
            request.task,
            request.step,
        )

        # If this message didn't carry enough real signal (e.g. a generic
        # "still stuck" follow-up), fall back to the last successful KB result
        # for this session instead of trusting a near-empty/unfocused search.
        if kb_result.get("low_signal") and session_id in _last_kb_result_by_session:
            kb_result = _last_kb_result_by_session[session_id]
        elif kb_result.get("found"):
            _last_kb_result_by_session[session_id] = kb_result

    history = get_session(session_id)

    # The LLM still gets full structured context -- this part was fine,
    # the bug was only ever in what got sent to the *search* step.
    ai_prompt = f"""
    Current Lab Context:
    Lab Name: {request.lab_name}
    Exercise: {request.exercise}
    Task: {request.task}
    Step: {request.step}

    User Question:
    {request.user_message}
    """

    ai_answer = generate_response(
        ai_prompt,
        kb_result["content"],
        history,
        casual=(question_type == "greeting"),
    )

    add_message(session_id, "assistant", ai_answer)

    log_chat_event(
        session_id=session_id,
        user_message=request.user_message,
        ai_answer=ai_answer,
        question_type=question_type,
        source=kb_result["source"],
        score=kb_result.get("score", 0),
        lab_context=lab_context
    )

    return {
        "session_id": session_id,
        "question_type": question_type,
        "answer": ai_answer,
        "source": kb_result["source"],
        "found": kb_result["found"],
        "score": kb_result.get("score", 0),
        "history": get_session(session_id),
        "lab_context": lab_context
    }


@app.delete("/session/{session_id}")
def delete_session(session_id: str):

    clear_session(session_id)

    if session_id in _last_kb_result_by_session:
        del _last_kb_result_by_session[session_id]

    return {
        "message": f"Session '{session_id}' cleared successfully."
    }
