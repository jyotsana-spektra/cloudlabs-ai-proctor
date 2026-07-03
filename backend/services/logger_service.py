import json
from datetime import datetime
from pathlib import Path

from backend.config import settings


def log_chat_event(
    session_id: str,
    user_message: str,
    ai_answer: str,
    question_type: str,
    source: str | None,
    score: int,
    lab_context: dict
) -> None:
    events_path = Path(settings.ANALYTICS_EVENTS_PATH)
    events_path.parent.mkdir(parents=True, exist_ok=True)

    if events_path.exists():
        try:
            with open(events_path, "r", encoding="utf-8") as file:
                events = json.load(file)
        except Exception:
            events = []
    else:
        events = []

    events.append({
        "timestamp": datetime.utcnow().isoformat(),
        "session_id": session_id,
        "question_type": question_type,
        "user_message": user_message,
        "ai_answer": ai_answer,
        "source": source,
        "score": score,
        "lab_context": lab_context
    })

    with open(events_path, "w", encoding="utf-8") as file:
        json.dump(events, file, indent=2)