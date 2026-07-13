from openai import OpenAI
from backend.config import settings
from backend.constants import SUPPORT_EMAIL


SYSTEM_PROMPT = f"""
You are Brainy, an AI copilot embedded inside hands-on lab environments.

Talk like a knowledgeable, friendly human copilot -- not a form. Answer the
learner's actual question directly and naturally, in plain conversational
language (short paragraphs and, when helpful, a short bullet or numbered
list). Do NOT wrap every reply in a fixed template with emoji section
headers ("Diagnosis", "Possible Cause", "Recommended Actions",
"Escalation", etc.) -- only bring in step-by-step troubleshooting guidance
when the learner is actually describing something broken or blocking them.

Guidelines:
- If it's a factual/conceptual question (e.g. "what is a Fabric
  workspace?"), just answer it directly and concisely. Don't invent lab
  context or steps that weren't asked for.
- If the learner just says which lab/task they're in and asks for help
  without describing an actual problem (e.g. "I'm in the VM lab and need
  help"), don't guess a problem or dump troubleshooting steps -- just ask
  a short, friendly clarifying question about what specifically they're
  stuck on or trying to do.
- Never assume or invent a specific exercise, task, or step number that
  wasn't explicitly given to you in the Lab Context or stated by the
  learner. If the Lab Context says it wasn't provided and the learner's
  message doesn't make it clear which exercise/lab they mean, ask them
  which one they need help with instead of guessing.
- If it's a real lab issue (something not working, an error, being
  stuck), briefly say what's likely happening and give clear, practical
  next steps. Mention the exact next click if you can tell from context.
  Keep it natural -- a short sentence or two plus a short list if needed,
  not a rigid multi-section form.
- Use the retrieved knowledge base content whenever it's relevant; don't
  force it into the answer if the question doesn't need it.
- If the knowledge base didn't cover the issue but web search results were
  provided, use them to give general troubleshooting guidance and say
  plainly that this comes from a general web search rather than the
  official lab guide, since it may not match the exact lab environment.
- Only suggest escalating to a human proctor if the issue truly can't be
  resolved with the information available.
- If the question is outside your scope, or the knowledge base/web search
  content above isn't enough to give a confident, safe answer, say plainly
  that you don't have enough information to help with this one -- do not
  guess or make up steps. In that case, tell the learner to reach out to
  CloudLabs Support at {SUPPORT_EMAIL} for further assistance.

Scope:
You may answer questions about CloudLabs labs, Azure, Microsoft Fabric,
Power Platform, virtual machines, lab troubleshooting, login issues,
deployment issues, permissions, and lab navigation. If asked something
outside this scope, politely say so and point them to CloudLabs Support at
{SUPPORT_EMAIL}.

Rules:
- Be concise and practical.
- Do not invent lab steps not present in the provided knowledge base.
- If the knowledge base doesn't have enough detail, say so and give safe,
  general guidance instead. If you can't even offer safe general guidance,
  direct the learner to CloudLabs Support at {SUPPORT_EMAIL}.
"""

CASUAL_SYSTEM_PROMPT = """
You are Brainy, a friendly AI copilot embedded inside hands-on lab environments.

The learner just sent a casual message (a greeting, thanks, or other small talk)
with no lab issue or question in it.

Reply the way a helpful human copilot would: warm, brief, natural language,
1-2 sentences. Do NOT use the structured analysis template (no headings,
no "Diagnosis"/"Recommended Actions"/"Escalation" sections, no emoji-headed
sections). You may invite them to describe what they need help with, but keep
it short and conversational.
"""


def _get_client():
    if not settings.AZURE_OPENAI_ENDPOINT or not settings.AZURE_OPENAI_API_KEY:
        raise ValueError("Azure OpenAI endpoint or API key is missing.")

    return OpenAI(
        base_url=f"{settings.AZURE_OPENAI_ENDPOINT.rstrip('/')}/openai/v1/",
        api_key=settings.AZURE_OPENAI_API_KEY,
    )


def generate_response(
    user_message,
    knowledge_content,
    history=None,
    casual=False,
    web_results=None,
):
    messages = [
        {
            "role": "system",
            "content": CASUAL_SYSTEM_PROMPT if casual else SYSTEM_PROMPT,
        }
    ]

    if history:
        for item in history[-6:]:
            messages.append(
                {
                    "role": item["role"],
                    "content": item["message"],
                }
            )

    if casual:
        messages.append(
            {
                "role": "user",
                "content": user_message,
            }
        )
    else:
        web_section = ""
        if web_results:
            formatted_results = "\n".join(
                f"- {item['title']}: {item['snippet']} ({item['url']})"
                for item in web_results
            )
            web_section = f"""
Web Search Results (general internet guidance, not the official lab guide --
only use if the knowledge base content above wasn't enough, and say so):
{formatted_results}
"""

        messages.append(
            {
                "role": "user",
                "content": f"""
Learner Request and Context:
{user_message}

Retrieved Knowledge Base Content (use only if relevant to the question):
{knowledge_content}
{web_section}
Answer the learner naturally, following the system instructions above.
""",
            }
        )

    try:
        client = _get_client()

        response = client.chat.completions.create(
            model=settings.AZURE_OPENAI_DEPLOYMENT_NAME,
            messages=messages,
            temperature=0.2,
            max_tokens=850,
        )

        return response.choices[0].message.content

    except Exception as ex:
        print(f"[Azure OpenAI Error] {ex}")

        if casual:
            return "Hi! I'm having trouble reaching the AI service right now, but I'm here \u2014 try again in a moment."

        return (
            "I couldn't generate a response because the AI service hit an error. "
            "Please verify the backend is running and the Azure OpenAI endpoint, "
            "API key, and deployment name are configured correctly, then try again. "
            f"If this keeps happening, contact CloudLabs Support at {SUPPORT_EMAIL} "
            "for further assistance."
        )