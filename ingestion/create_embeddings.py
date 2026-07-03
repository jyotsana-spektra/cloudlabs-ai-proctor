"""
Embedding generation for CloudLabs AI Proctor.

Current MVP:
Creates placeholder embeddings.

Future:
Replace with Azure OpenAI text-embedding model.
"""

from typing import List


def create_embedding(text: str) -> List[float]:
    """
    Create a placeholder embedding.

    Future implementation:
    Azure OpenAI Embeddings API.
    """

    return [0.0] * 1536


def generate_embeddings(chunks: List[dict]) -> List[dict]:
    """
    Attach embeddings to document chunks.
    """

    results = []

    for chunk in chunks:

        chunk["embedding"] = create_embedding(chunk["text"])

        results.append(chunk)

    return results


if __name__ == "__main__":

    sample = [
        {
            "text": "VM not loading."
        }
    ]

    print(generate_embeddings(sample))
