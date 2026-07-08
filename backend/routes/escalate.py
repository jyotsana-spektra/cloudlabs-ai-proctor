from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.escalation_service import (
    save_escalation,
    get_escalations,
)

router = APIRouter()


class EscalationRequest(BaseModel):
    session_id: str
    issue_summary: str
    lab_id: str | None = None
    lab_name: str | None = None
    exercise: str | None = None
    task: str | None = None
    step: str | None = None


@router.post("/")
def create_escalation(request: EscalationRequest):
    return save_escalation(
        request.session_id,
        request.issue_summary,
        request.lab_id,
        request.lab_name,
        request.exercise,
        request.task,
        request.step,
    )


@router.get("/")
def list_escalations():
    return get_escalations()