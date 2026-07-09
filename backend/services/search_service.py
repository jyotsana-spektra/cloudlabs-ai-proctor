from pathlib import Path

from backend.utils.chunking import chunk_text


# Generic words that show up in almost every lab-guide/troubleshooting doc.
# These must NEVER be allowed to drive relevance scoring on their own.
STOPWORDS = {
    "the", "and", "for", "with", "this", "that", "what", "when", "where",
    "how", "why", "who", "which", "you", "your", "are", "was", "were",
    "have", "has", "had", "not", "but", "can", "will", "would", "could",
    "should", "please", "help", "issue", "problem", "still", "already",
    "happening", "waited", "minutes", "currently", "current",
}

# Only used as a metadata boost when the user's ACTUAL question mentions
# a specific technology/action term -- not boilerplate labels like
# "task"/"step"/"lab name" which appear in every request regardless of topic.
PRIORITY_KEYWORDS = {
    "vm", "login", "fabric", "lakehouse", "eventhouse", "agent",
    "deployment", "access", "browser", "portal", "workspace",
    "permission", "credential", "password", "timeout", "error",
}


def _extract_keywords(text: str) -> list[str]:
    words = [
        w.strip().lower().strip(".,:;!?()[]{}\"'")
        for w in text.replace("\n", " ").split()
    ]
    return [w for w in words if len(w) > 2 and w not in STOPWORDS]


def search_knowledge_base(
    question: str,
    question_type: str,
    lab_id: str | None = None,
    task: str | None = None,
    step: str | None = None,
) -> dict:
    """
    IMPORTANT: `question` must be the learner's RAW message only.
    Do NOT pass a template string containing labels like
    "Lab Name:", "Task:", "Step:" -- those labels pollute keyword
    scoring because they appear in every single request regardless
    of topic. Use the `lab_id` / `task` / `step` params below instead,
    which are matched separately as structured metadata.
    """
    kb_path = Path("knowledge-base")

    folders_to_search = []

    if lab_id:
        folders_to_search.append(kb_path / "labguides" / lab_id)

    folders_to_search.extend([
        kb_path / "labguides",
        kb_path / "troubleshooting",
        kb_path / "known-issues",
        kb_path / "faqs",
    ])

    keywords = _extract_keywords(question)

    # If the message carries almost no real signal (e.g. a generic
    # "still stuck" style follow-up), say so explicitly instead of
    # letting scoring fall back to noise. The caller (main.py) should
    # treat this as "re-use the previous answer's context" rather than
    # blindly re-searching.
    if len(keywords) < 2:
        return {
            "found": False,
            "source": None,
            "content": (
                "The learner's message did not contain enough specific "
                "detail to search the knowledge base. Ask a clarifying "
                "question, or if this is a follow-up, refer back to the "
                "previous diagnosis and ask what specifically did not work."
            ),
            "score": 0,
            "low_signal": True,
        }

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
                file_lower = str(md_file).lower()

                for chunk in chunks:
                    chunk_lower = chunk.lower()
                    score = 0

                    for keyword in keywords:
                        if keyword in chunk_lower:
                            score += 1
                        if keyword in file_lower:
                            score += 1

                    for priority in PRIORITY_KEYWORDS:
                        if priority in keywords and priority in chunk_lower:
                            score += 2

                    # Structured metadata match -- these come from actual
                    # session/lab context, not from parsing question text,
                    # so they can't be polluted by template labels.
                    if task and task.lower() in file_lower:
                        score += 3
                    if step and step.lower() in chunk_lower:
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
            "score": best_score,
            "low_signal": False,
        }

    return {
        "found": False,
        "source": None,
        "content": (
            "No strong matching lab content was found. "
            "Use the provided lab name, exercise, task, step, and user issue "
            "to ask a focused follow-up question and provide general troubleshooting guidance."
        ),
        "score": best_score,
        "low_signal": False,
    }
