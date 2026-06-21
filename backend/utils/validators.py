def validate_chat_request(user_message: str) -> dict:
    if not user_message or not user_message.strip():
        return {
            "valid": False,
            "error": "User message cannot be empty."
        }

    return {
        "valid": True,
        "error": None
    }
