import json
from datetime import datetime
from pathlib import Path

from backend.config import settings


def _load_feedback():
    feedback_path = Path(settings.ANALYTICS_FEEDBACK_PATH)
    feedback_path.parent.mkdir(parents=True, exist_ok=True)

    if not feedback_path.exists():
        return []

    try:
        with open(feedback_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_feedback(
    session_id: str,
    user_message: str,
    answer: str,
    rating: int,
):
    feedback_path = Path(settings.ANALYTICS_FEEDBACK_PATH)

    feedback = _load_feedback()

    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "session_id": session_id,
        "user_message": user_message,
        "answer": answer,
        "rating": rating,
    }

    feedback.append(entry)

    with open(feedback_path, "w", encoding="utf-8") as f:
        json.dump(feedback, f, indent=2)

    return {
        "success": True,
        "message": "Feedback saved successfully",
    }


def get_feedback():
    return {
        "feedback": _load_feedback()
    }