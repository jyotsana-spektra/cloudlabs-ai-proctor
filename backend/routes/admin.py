from pathlib import Path

from fastapi import APIRouter

from backend.config import settings

router = APIRouter()


@router.get("/status")
def admin_status():
    return {
        "status": "Admin route is available"
    }


@router.get("/labs")
def list_labs():
    """
    Lists the available lab-guide workshop folders in the knowledge base
    (e.g. "fabric", "virtual-machine-and-compute"), so the frontend can let
    learners pick which workshop they're in. That selection is sent back as
    `lab_id` on /chat, which scopes the knowledge-base search to that folder.
    """
    labguides_path = Path(settings.KNOWLEDGE_BASE_PATH) / "labguides"

    if not labguides_path.exists():
        return {"labs": []}

    labs = [
        {
            "id": folder.name,
            "label": folder.name.replace("-", " ").title(),
        }
        for folder in labguides_path.iterdir()
        if folder.is_dir()
    ]

    labs.sort(key=lambda item: item["label"])

    return {"labs": labs}
