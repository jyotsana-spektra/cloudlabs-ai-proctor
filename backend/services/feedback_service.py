feedback_store = []


def save_feedback(
    session_id: str,
    user_message: str,
    answer: str,
    rating: int
):
    feedback_store.append(
        {
            "session_id": session_id,
            "user_message": user_message,
            "answer": answer,
            "rating": rating
        }
    )

    return {
        "success": True
    }


def get_feedback():

    return feedback_store
