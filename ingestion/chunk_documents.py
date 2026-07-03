"""
Document chunking utilities for CloudLabs AI Proctor.

Splits Markdown documents into smaller chunks suitable for
search indexing and future embedding generation.
"""

from typing import List


CHUNK_SIZE = 800


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE) -> List[str]:
    """
    Split text into fixed-size chunks.

    Args:
        text: Document text.
        chunk_size: Maximum characters per chunk.

    Returns:
        List of text chunks.
    """

    text = text.strip()

    if not text:
        return []

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks


def chunk_document(document: dict) -> List[dict]:
    """
    Split a parsed document into searchable chunks.
    """

    chunks = []

    content = document.get("content", "")
    metadata = document.get("metadata", {})

    for index, chunk in enumerate(chunk_text(content), start=1):

        chunks.append({
            "chunk_id": index,
            "text": chunk,
            "title": document.get("title"),
            "file_name": document.get("file_name"),
            "metadata": metadata
        })

    return chunks


def chunk_documents(documents: List[dict]) -> List[dict]:
    """
    Chunk multiple documents.
    """

    results = []

    for document in documents:
        results.extend(chunk_document(document))

    return results


if __name__ == "__main__":

    sample = {
        "title": "VM Not Loading",
        "file_name": "vm-not-loading.md",
        "content": "Hello " * 500,
        "metadata": {}
    }

    chunks = chunk_document(sample)

    print(f"Generated {len(chunks)} chunks.")
