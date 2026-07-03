import os
from openai import OpenAI
from backend.config import settings


client = OpenAI(
    base_url=f"{settings.AZURE_OPENAI_ENDPOINT}/openai/v1/",
    api_key=settings.AZURE_OPENAI_API_KEY,
)


SYSTEM_PROMPT = """
You are CloudLabs AI Proctor.

Your role is to help users complete CloudLabs hands-on labs.

Rules:
- Answer ONLY questions related to CloudLabs labs, Azure, Microsoft Fabric, virtual machines, troubleshooting, and the provided knowledge base.
- If the question is outside the CloudLabs domain, politely explain that it is outside your scope.
- Use the supplied knowledge base content whenever possible.
- Never tell the user to contact a human proctor.
- Give concise, actionable troubleshooting steps.
"""


def generate_response(user_message, knowledge_content, history=None):
    """
    Generate an AI response using Azure OpenAI.
    """

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ]

    # Previous conversation
    if history:
        for item in history[-6:]:
            messages.append(
                {
                    "role": item["role"],
                    "content": item["message"],
                }
            )

    # Current request
    messages.append(
        {
            "role": "user",
            "content": f"""
User Question:
{user_message}

Knowledge Base:
{knowledge_content}
""",
        }
    )

    try:
        response = client.chat.completions.create(
            model=settings.AZURE_OPENAI_DEPLOYMENT_NAME,
            messages=messages,
            temperature=0.2,
            max_tokens=700,
        )

        return response.choices[0].message.content

    except Exception as ex:
        print(f"[Azure OpenAI Error] {ex}")

        return (
            "Sorry, I encountered an internal AI service error while "
            "generating a response. Please try again."
        )