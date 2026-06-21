from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.ingestion_service import (
    ingest_local_lab,
    ingest_github_markdown,
    ingest_github_repository
)

router = APIRouter()


class LocalLabIngestRequest(BaseModel):
    source_folder: str
    lab_id: str


class GithubMarkdownRequest(BaseModel):
    raw_file_url: str
    lab_id: str
    file_name: str


class GithubRepositoryRequest(BaseModel):
    repo_url: str
    lab_id: str


@router.post("/ingest-local-lab")
def ingest_local_lab_route(request: LocalLabIngestRequest):
    return ingest_local_lab(
        request.source_folder,
        request.lab_id
    )


@router.post("/ingest-github-markdown")
def ingest_github_markdown_route(request: GithubMarkdownRequest):
    return ingest_github_markdown(
        request.raw_file_url,
        request.lab_id,
        request.file_name
    )


@router.post("/ingest-github-repository")
def ingest_github_repository_route(request: GithubRepositoryRequest):
    return ingest_github_repository(
        request.repo_url,
        request.lab_id
    )