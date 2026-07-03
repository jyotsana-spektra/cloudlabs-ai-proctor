"""
Metadata extraction utilities for CloudLabs AI Proctor ingestion pipeline.
"""

from pathlib import Path


def extract_metadata(document: dict) -> dict:
    """
    Extract metadata from a parsed Markdown document.
    """
    file_path = Path(document.get("file_path", ""))

    folder = file_path.parent.name if file_path.parent else "unknown"

    headings = document.get("headings", [])

    return {
        "title": document.get("title"),
        "file_name": document.get("file_name"),
        "file_path": document.get("file_path"),
        "folder": folder,
        "headings": headings,
        "tags": generate_tags(document),
    }


def generate_tags(document: dict) -> list[str]:
    """
    Generate simple tags based on file path and content.
    """
    text = (
        document.get("file_name", "")
        + " "
        + document.get("file_path", "")
        + " "
        + document.get("content", "")
    ).lower()

    tags = []

    keyword_map = {
        "vm": "vm",
        "virtual machine": "vm",
        "login": "login",
        "authentication": "login",
        "fabric": "fabric",
        "lakehouse": "fabric",
        "eventhouse": "fabric",
        "agent": "agent",
        "deployment": "deployment",
        "access denied": "access",
        "permission": "access",
        "browser": "browser",
        "power automate": "power-automate",
    }

    for keyword, tag in keyword_map.items():
        if keyword in text and tag not in tags:
            tags.append(tag)

    return tags


def attach_metadata(document: dict) -> dict:
    """
    Attach metadata to a document.
    """
    document["metadata"] = extract_metadata(document)
    return document
