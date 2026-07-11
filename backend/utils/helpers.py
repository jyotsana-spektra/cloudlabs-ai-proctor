import re
from datetime import datetime


def current_timestamp():

    return datetime.now().isoformat()


_LAB_REFERENCE_PATTERNS = {
    "lab": r"\blab\s*#?\s*(\d+)\b",
    "exercise": r"\bexercise\s*#?\s*(\d+)\b",
    "task": r"\btask\s*#?\s*(\d+)\b",
    "step": r"\bstep\s*#?\s*(\d+)\b",
}


def extract_lab_references(text: str) -> dict:
    """
    Parse free-text learner messages like "I am stuck on lab 1 task 2 step 3"
    and pull out the lab/exercise/task/step numbers mentioned. This lets the
    search layer match numbered lab-guide files even when the caller didn't
    pass structured lab_id/task/step metadata (or the frontend only sent
    generic placeholder values).

    Returns a dict with any of the keys "lab", "exercise", "task", "step"
    that were found, mapped to the referenced number as a string.
    """
    if not text:
        return {}

    lowered = text.lower()
    references = {}

    for key, pattern in _LAB_REFERENCE_PATTERNS.items():
        match = re.search(pattern, lowered)
        if match:
            references[key] = match.group(1)

    return references