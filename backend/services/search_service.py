import re
from pathlib import Path

from backend.utils.chunking import chunk_text
from backend.utils.helpers import extract_lab_references


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
    # Numeric tokens (e.g. the "1" in "lab 1") and known priority terms
    # (e.g. "vm") must be kept even though they're short -- they're exactly
    # what tells us WHICH lab/task/step the learner means, or what specific
    # technology/issue they're hitting. Everything else still needs len > 2
    # to avoid noise.
    return [
        w for w in words
        if w and w not in STOPWORDS
        and (len(w) > 2 or w.isdigit() or w in PRIORITY_KEYWORDS)
    ]


def _file_matches_number(file_stem: str, number: str) -> bool:
    """
    Matches numbered lab-guide filenames -- e.g. "lab3", "lab-3",
    "exercise3", "03-delta-lake", "3-delta-lake" -- against a lab/exercise
    number the learner mentioned in free text ("lab 3", "exercise 3").
    """
    stem = file_stem.lower()
    padded = number.zfill(2)

    patterns = [
        rf"^lab-?0*{number}$",
        rf"^exercise-?0*{number}$",
        rf"^0*{number}[-_]",
        rf"^{padded}[-_]",
    ]
    return any(re.match(pattern, stem) for pattern in patterns)


def _extract_number(text: str | None) -> str | None:
    """Pulls the first digit sequence out of a label like "Exercise 2" so it
    can be matched against numbered lab-guide filenames (exercise2.md)."""
    if not text:
        return None
    match = re.search(r"\d+", text)
    return match.group(0) if match else None


def _score_chunk(
    chunk_lower: str,
    file_lower: str,
    file_stem: str,
    keywords: list[str],
    references: dict,
    lab_id: str | None,
    exercise: str | None,
    task: str | None,
    step: str | None,
) -> int:
    score = 0

    for keyword in keywords:
        if keyword in chunk_lower:
            score += 1
        if keyword in file_lower:
            score += 1

    for priority in PRIORITY_KEYWORDS:
        if priority in keywords and priority in chunk_lower:
            score += 2

    # Structured metadata match -- these come from actual session/lab
    # context, not from parsing question text, so they can't be polluted
    # by template labels.
    if exercise and exercise.lower() in file_lower:
        score += 3
    if task and task.lower() in file_lower:
        score += 3
    if step and step.lower() in chunk_lower:
        score += 2
    if lab_id and lab_id.lower() in file_lower:
        score += 3

    # The structured `exercise` field (from the UI's lab-context selector,
    # not free text) is the strongest signal for WHICH numbered lab-guide
    # file to use (exercise2.md, lab3.md, 03-delta-lake.md...) -- it must be
    # applied even when the learner's own message never repeats the number
    # (e.g. they just ask "why isn't this working" while Exercise 2 is
    # selected in the sidebar).
    exercise_number = _extract_number(exercise)
    if exercise_number and _file_matches_number(file_stem, exercise_number):
        score += 5

    # Numbered references parsed from the learner's raw message (e.g.
    # "lab 1"/"exercise 1" -> lab1.md, 01-lakehouse.md). Weighted heavily
    # since a filename match on the exact lab/exercise number is a very
    # strong signal of relevance.
    lab_number = references.get("lab") or references.get("exercise")
    if lab_number and _file_matches_number(file_stem, lab_number):
        score += 5
    if references.get("task") and references["task"] in chunk_lower:
        score += 2
    if references.get("step") and references["step"] in chunk_lower:
        score += 2

    return score


def _search_folders(
    folders: list[Path],
    keywords: list[str],
    references: dict,
    lab_id: str | None,
    exercise: str | None,
    task: str | None,
    step: str | None,
) -> tuple[Path | None, int, str]:
    best_match = None
    best_score = 0
    best_chunk = ""

    for folder in folders:
        if not folder.exists():
            continue

        for md_file in folder.rglob("*.md"):
            try:
                content = md_file.read_text(encoding="utf-8", errors="ignore")
                chunks = chunk_text(content)
                file_lower = str(md_file).lower()
                file_stem = md_file.stem.lower()

                for chunk in chunks:
                    score = _score_chunk(
                        chunk.lower(),
                        file_lower,
                        file_stem,
                        keywords,
                        references,
                        lab_id,
                        exercise,
                        task,
                        step,
                    )

                    if score > best_score:
                        best_score = score
                        best_match = md_file
                        best_chunk = chunk

            except Exception:
                continue

    return best_match, best_score, best_chunk


def search_knowledge_base(
    question: str,
    question_type: str,
    lab_id: str | None = None,
    exercise: str | None = None,
    task: str | None = None,
    step: str | None = None,
) -> dict:
    """
    IMPORTANT: `question` must be the learner's RAW message only.
    Do NOT pass a template string containing labels like
    "Lab Name:", "Task:", "Step:" -- those labels pollute keyword
    scoring because they appear in every single request regardless
    of topic. Use the `lab_id` / `exercise` / `task` / `step` params below
    instead, which are matched separately as structured metadata. All four
    fields (when provided) are always applied together so the retrieved
    content is scoped to the exact lab, exercise, task, AND step the
    learner is on -- never just a subset of them.
    """
    kb_path = Path("knowledge-base")

    keywords = _extract_keywords(question)

    # If the message carries almost no real signal (e.g. a generic
    # "still stuck"/"i need help" style message), the raw text itself can't
    # drive a keyword search. But if the learner has a real, specific
    # exercise selected (ideally with task/step too), we still know exactly
    # which part of the lab guide they're on -- so look that up directly,
    # scoped purely by the structured lab_id/exercise/task/step metadata
    # (no keyword requirement at all). This lets Brainy ask a specific,
    # informed clarifying question grounded in what that step actually asks
    # the learner to do, instead of a generic "what are you stuck on?".
    if len(keywords) < 2:
        if lab_id and exercise:
            lab_folder = kb_path / "labguides" / lab_id
            best_match, best_score, best_chunk = _search_folders(
                [lab_folder], [], {}, lab_id, exercise, task, step
            )

            if best_match and best_score > 0:
                return {
                    "found": True,
                    "source": str(best_match),
                    "content": best_chunk,
                    "score": best_score,
                    "low_signal": True,
                    "context_only": True,
                }

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

    # Pull explicit "lab 1" / "exercise 2" / "task 3" / "step 4" style
    # references straight out of the learner's own message. This works even
    # when the caller didn't pass structured lab_id/task/step (or the
    # frontend only sent generic placeholder values), and lets us pinpoint
    # numbered lab-guide files (lab3.md, exercise2.md, 03-delta-lake.md...).
    references = extract_lab_references(question)

    # If we know which workshop the learner is in, search that folder
    # FIRST and in isolation. This is what actually resolves "lab 1" to
    # the right file: without scoping, a same-numbered file in a totally
    # different workshop (e.g. Fabric's Exercise-1.md) can outscore the
    # intended match just by having more matching words in its body text.
    if lab_id:
        lab_folder = kb_path / "labguides" / lab_id
        best_match, best_score, best_chunk = _search_folders(
            [lab_folder], keywords, references, lab_id, exercise, task, step
        )

        if best_match and best_score >= 3:
            return {
                "found": True,
                "source": str(best_match),
                "content": best_chunk,
                "score": best_score,
                "low_signal": False,
            }

    # Fall back to a broad search across the whole knowledge base -- no
    # lab_id was given, the lab_id folder doesn't exist, or nothing strong
    # enough was found scoped to it.
    all_folders = [
        kb_path / "labguides",
        kb_path / "troubleshooting",
        kb_path / "known-issues",
        kb_path / "faqs",
    ]

    best_match, best_score, best_chunk = _search_folders(
        all_folders, keywords, references, lab_id, exercise, task, step
    )

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
