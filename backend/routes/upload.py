from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.ingestion_service import ingest_local_lab

router = APIRouter()


class LocalLabIngestRequest(BaseModel):
    source_folder: str
    lab_id: str


@router.post("/ingest-local-lab")
def ingest_local_lab_route(request: LocalLabIngestRequest):
    return ingest_local_lab(
        request.source_folder,
        request.lab_id
    )
