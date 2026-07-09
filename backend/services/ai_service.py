from openai import OpenAI
from backend.config import settings


SYSTEM_PROMPT = """
You are CloudLabs AI Proctor, an AI copilot embedded inside hands-on lab environments.

Your job is not to behave like a generic chatbot. Your job is to act like a real lab proctor:
- Understand the learner's current lab, exercise, task, step, and screen context.
- Use the retrieved knowledge base content whenever available.
- Diagnose what is likely blocking the learner.
- Give clear next actions and the exact next click when possible.
- Keep the learner moving through the lab.
- Escalate only when the issue cannot be resolved with available information.

Scope:
You may answer questions about CloudLabs labs, Azure, Microsoft Fabric, Power Platform, virtual machines, lab troubleshooting, login issues, deployment issues, permissions, and lab navigation.

If the question is outside this scope, politely say it is outside the CloudLabs AI Proctor scope.

Response format:
Always respond in this structure:

🧠 AI Proctor Analysis

📍 Current Context
- Lab:
- Exercise:
- Task:
- Step:

🔍 Diagnosis
Explain what is likely happening in 1-2 lines.

⚠️ Possible Cause
Explain the most likely cause briefly.

✅ Recommended Actions
1.
2.
3.

➡️ Next Click
Tell the learner exactly what to click next. If unknown, say what they should check next.

🆘 Escalation
Only recommend escalation if the issue persists after the steps, permissions are missing, or the lab environment appears broken.

Rules:
- Be concise.
- Be practical.
- Do not invent lab steps not present in the provided knowledge base.
- If the knowledge base does not contain enough detail, say so clearly and give safe troubleshooting guidance.
- Do not tell the user to contact a human proctor unless escalation is truly needed.
"""


def _get_client():
    if not settings.AZURE_OPENAI_ENDPOINT or not settings.AZURE_OPENAI_API_KEY:
        raise ValueError("Azure OpenAI endpoint or API key is missing.")

    return OpenAI(
        base_url=f"{settings.AZURE_OPENAI_ENDPOINT.rstrip('/')}/openai/v1/",
        api_key=settings.AZURE_OPENAI_API_KEY,
    )


def generate_response(user_message, knowledge_content, history=None):
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
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

    messages.append(
        {
            "role": "user",
            "content": f"""
Learner Request and Context:
{user_message}

Retrieved Knowledge Base Content:
{knowledge_content}

Generate a CloudLabs AI Proctor response using the required response format.
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

        return (
            "🧠 AI Proctor Analysis\n\n"
            "📍 Current Context\n"
            "- Lab: Not available\n"
            "- Exercise: Not available\n"
            "- Task: Not available\n"
            "- Step: Not available\n\n"
            "🔍 Diagnosis\n"
            "I could not generate a response because the AI service encountered an error.\n\n"
            "⚠️ Possible Cause\n"
            "Azure OpenAI configuration, deployment name, or network connectivity may be unavailable.\n\n"
            "✅ Recommended Actions\n"
            "1. Verify the backend is running.\n"
            "2. Check the Azure OpenAI endpoint, API key, and deployment name.\n"
            "3. Retry the request after restarting the backend.\n\n"
            "➡️ Next Click\n"
            "Open the backend logs and check the Azure OpenAI error.\n\n"
            "🆘 Escalation\n"
            "Escalate only if the configuration is correct and the issue still persists."
        )