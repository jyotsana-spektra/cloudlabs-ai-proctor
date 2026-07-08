from pathlib import Path

from backend.utils.chunking import chunk_text


def search_knowledge_base(
    question: str,
    question_type: str,
    lab_id: str | None = None
) -> dict:
    kb_path = Path("knowledge-base")

    folders_to_search = []

    if lab_id:
        folders_to_search.append(kb_path / "labguides" / lab_id)

    folders_to_search.extend([
        kb_path / "labguides",
        kb_path / "troubleshooting",
        kb_path / "known-issues",
        kb_path / "faqs"
    ])

    keywords = [
        word.strip().lower()
        for word in question.replace("\n", " ").split()
        if len(word.strip()) > 2
    ]

    priority_keywords = [
        "exercise",
        "task",
        "step",
        "lab",
        "workspace",
        "vm",
        "login",
        "fabric",
        "lakehouse",
        "eventhouse",
        "agent",
        "deployment",
        "access",
        "browser"
    ]

    best_match = None
    best_score = 0
    best_chunk = ""

    for folder in folders_to_search:
        if not folder.exists():
            continue

        for md_file in folder.rglob("*.md"):
            try:
                content = md_file.read_text(encoding="utf-8", errors="ignore")
                chunks = chunk_text(content)

                for chunk in chunks:
                    chunk_lower = chunk.lower()
                    file_lower = str(md_file).lower()

                    score = 0

                    for keyword in keywords:
                        if keyword in chunk_lower:
                            score += 1
                        if keyword in file_lower:
                            score += 1

                    for priority in priority_keywords:
                        if priority in question.lower() and priority in chunk_lower:
                            score += 2

                    if lab_id and lab_id.lower() in file_lower:
                        score += 3

                    if score > best_score:
                        best_score = score
                        best_match = md_file
                        best_chunk = chunk

            except Exception:
                continue

    if best_match and best_score >= 3:
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
            "No strong matching lab content was found. "
            "Use the provided lab name, exercise, task, step, and user issue "
            "to ask a focused follow-up question and provide general troubleshooting guidance."
        ),
        "score": best_score
    }