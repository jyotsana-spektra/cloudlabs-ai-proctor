from pydantic import BaseModel


class ChatRequest(BaseModel):
    user_message: str
    session_id: str | None = "default"

    lab_id: str | None = None
    lab_name: str | None = None
    exercise: str | None = None
    task: str | None = None
    step: str | None = None
