from pathlib import Path

from backend.utils.chunking import chunk_text


def search_knowledge_base(
    question: str,
    question_type: str,
    lab_id: str | None = None
) -> dict:
    kb_path = Path("knowledge-base")

    if question_type == "troubleshooting":
        folders_to_search = [
            kb_path / "troubleshooting",
            kb_path / "known-issues"
        ]

    elif question_type == "lab_help":
        if lab_id:
            folders_to_search = [
                kb_path / "labguides" / lab_id
            ]
        else:
            folders_to_search = [
                kb_path / "labguides"
            ]

    else:
        folders_to_search = [
            kb_path / "faqs"
        ]

    keywords = question.lower().split()

    best_match = None
    best_score = 0
    best_chunk = ""

    for folder in folders_to_search:
        if not folder.exists():
            continue

        for md_file in folder.rglob("*.md"):
            with open(md_file, "r", encoding="utf-8") as file:
                content = file.read()

            chunks = chunk_text(content)

            for chunk in chunks:
                chunk_lower = chunk.lower()
                score = 0

                for keyword in keywords:
                    if keyword in chunk_lower:
                        score += 1

                if score > best_score:
                    best_score = score
                    best_match = md_file
                    best_chunk = chunk

    if best_match:
        return {
            "found": True,
            "source": str(best_match),
            "content": best_chunk,
            "score": best_score
        }

    return {
        "found": False,
        "source": None,
        "content": (
            "No relevant information was found in the knowledge base. "
            "Please provide the lab name, exercise, task, step number, "
            "and exact error message so troubleshooting can continue."
        ),
        "score": 0
    }