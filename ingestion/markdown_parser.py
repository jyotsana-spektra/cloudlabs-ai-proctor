"""
Markdown parser for CloudLabs AI Proctor ingestion pipeline.
"""

from pathlib import Path


def parse_markdown(file_path: str | Path) -> dict:
    """
    Parse a Markdown file into structured content.
    """
    path = Path(file_path)
    content = path.read_text(encoding="utf-8", errors="ignore")

    lines = content.splitlines()
    title = path.stem

    for line in lines:
        if line.startswith("# "):
            title = line.replace("# ", "").strip()
            break

    headings = [
        line.strip()
        for line in lines
        if line.startswith("#")
    ]

    return {
        "title": title,
        "file_name": path.name,
        "file_path": str(path),
        "headings": headings,
        "content": content,
    }


def parse_markdown_documents(file_paths: list[Path]) -> list[dict]:
    """
    Parse multiple Markdown files.
    """
    return [parse_markdown(path) for path in file_paths]
