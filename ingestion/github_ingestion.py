"""
GitHub ingestion utilities for CloudLabs AI Proctor.

This module is responsible for collecting Markdown documentation from
GitHub repositories or local cloned repositories.
"""

from pathlib import Path
from typing import List


def collect_markdown_files(source_path: str) -> List[Path]:
    """
    Collect all Markdown files from a local repository or folder.

    Args:
        source_path: Path to a local repository or documentation folder.

    Returns:
        List of Markdown file paths.
    """
    source = Path(source_path)

    if not source.exists():
        raise FileNotFoundError(f"Source path not found: {source_path}")

    markdown_files = list(source.rglob("*.md"))

    return markdown_files


def read_markdown_file(file_path: Path) -> dict:
    """
    Read a Markdown file and return basic document data.
    """
    content = file_path.read_text(encoding="utf-8", errors="ignore")

    return {
        "file_name": file_path.name,
        "file_path": str(file_path),
        "content": content,
    }


def ingest_local_repository(source_path: str) -> List[dict]:
    """
    Ingest all Markdown files from a local repository.

    Args:
        source_path: Local repository path.

    Returns:
        List of parsed Markdown document dictionaries.
    """
    documents = []

    for file_path in collect_markdown_files(source_path):
        documents.append(read_markdown_file(file_path))

    return documents


if __name__ == "__main__":
    docs = ingest_local_repository("knowledge-base")
    print(f"Ingested {len(docs)} Markdown documents.")
