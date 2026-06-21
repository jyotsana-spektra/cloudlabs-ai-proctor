def generate_response(user_message, knowledge_content, history=None):

    response = ""

    if history and len(history) > 0:

        previous_context = "\n".join(
            [
                f"{msg['role']}: {msg['message']}"
                for msg in history[-5:]
            ]
        )

        response += (
            "Conversation context:\n"
            + previous_context
            + "\n\n"
        )

    response += (
        "Based on the available information:\n\n"
        + knowledge_content
    )

    return response