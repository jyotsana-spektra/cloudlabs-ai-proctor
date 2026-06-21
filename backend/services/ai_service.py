def generate_response(question: str, knowledge_content: str) -> str:

    response = f"""
It appears that you're experiencing the following issue:

{question}

Based on the information available, please review the following guidance:

{knowledge_content}

Please try the recommended steps one at a time.

If the issue still persists, tell me:

• The exact error message
• The current exercise, task, and step
• What you have already tried

I will continue troubleshooting and help you resolve the issue.
"""

    return response.strip()