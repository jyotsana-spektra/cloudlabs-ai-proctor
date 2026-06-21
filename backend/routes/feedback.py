from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.feedback_service import save_feedback, get_feedback

router = APIRouter()


class FeedbackRequest(BaseModel):
    session_id: str
    user_message: str
    answer: str
    rating: int


@router.post("/")
def submit_feedback(request: FeedbackRequest):
    return save_feedback(
        request.session_id,
        request.user_message,
        request.answer,
        request.rating
    )


@router.get("/")
def list_feedback():
    return get_feedback()
