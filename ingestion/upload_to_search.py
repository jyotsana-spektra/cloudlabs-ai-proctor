"""
Upload processed documents.

Current MVP:
Stores processed chunks locally.

Future:
Upload to Azure AI Search.
"""

import json
from pathlib import Path


OUTPUT_FILE = "analytics/search_index.json"


def upload_documents(documents: list[dict]):

    output = Path(OUTPUT_FILE)

    output.parent.mkdir(parents=True, exist_ok=True)

    with open(output, "w", encoding="utf-8") as file:
        json.dump(documents, file, indent=2)

    return {
        "documents_uploaded": len(documents),
        "output_file": OUTPUT_FILE
    }


if __name__ == "__main__":

    sample = [
        {
            "title": "VM",
            "text": "VM not loading."
        }
    ]

    print(upload_documents(sample))
