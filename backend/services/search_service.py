from pathlib import Path


def search_knowledge_base(question: str, question_type: str) -> dict:
    kb_path = Path("knowledge-base")

    if question_type == "troubleshooting":
        folders_to_search = [
            kb_path / "troubleshooting",
            kb_path / "known-issues"
        ]

    elif question_type == "lab_help":
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
    best_content = ""

    for folder in folders_to_search:
        if not folder.exists():
            continue

        for md_file in folder.rglob("*.md"):
            with open(md_file, "r", encoding="utf-8") as file:
                content = file.read()

            content_lower = content.lower()
            score = 0

            for keyword in keywords:
                if keyword in content_lower:
                    score += 1

            if score > best_score:
                best_score = score
                best_match = md_file
                best_content = content

    if best_match:
        return {
            "found": True,
            "source": str(best_match),
            "content": best_content
        }

    return {
        "found": False,
        "source": None,
        "content": (
            "No relevant information was found in the knowledge base. "
            "Please provide the lab name, exercise, task, step number, "
            "and exact error message so troubleshooting can continue."
        )
    }