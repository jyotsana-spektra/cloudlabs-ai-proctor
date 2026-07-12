import re

GREETING_PHRASES = {
    "hi", "hii", "hiii", "hello", "hey", "heyy", "yo",
    "good morning", "good afternoon", "good evening",
    "thanks", "thank you", "thx", "ty",
    "bye", "goodbye", "see you", "ok", "okay", "cool", "great", "nice",
}

# Words that actually indicate something is broken/blocking the learner.
# Kept narrow on purpose -- topic words like "vm", "login", "browser" are
# NOT included here because they show up constantly in messages that are
# just describing *where* the learner is (e.g. "I am in the azure vm lab
# and need help"), which is not a problem report and shouldn't trigger the
# troubleshooting UI/template.
TROUBLESHOOTING_KEYWORDS = [
    "error",
    "errors",
    "fail",
    "failed",
    "failing",
    "failure",
    "issue",
    "problem",
    "cannot",
    "can't",
    "cant",
    "won't",
    "wont",
    "doesn't work",
    "doesnt work",
    "not working",
    "not loading",
    "not responding",
    "not connecting",
    "not starting",
    "stuck",
    "denied",
    "timeout",
    "timed out",
    "crash",
    "crashed",
    "broken",
    "unable",
]

# Topic words that mean the learner is talking about the lab, but on their
# own don't indicate a broken/failing state -- just route these to a plain,
# natural "lab help" response instead of the troubleshooting template.
LAB_KEYWORDS = [
    "exercise",
    "task",
    "step",
    "workspace",
    "lakehouse",
    "eventhouse",
    "ontology",
    "agent",
    "fabric",
    "vm",
    "virtual machine",
    "compute",
    "login",
    "browser",
    "portal",
]


def _contains_phrase(text: str, phrase: str) -> bool:
    if " " in phrase:
        return phrase in text
    return re.search(rf"\b{re.escape(phrase)}\b", text) is not None


def classify_question(question: str) -> str:

    question = question.lower().strip().strip(".,!?")

    # Casual chit-chat (greetings/thanks/acknowledgements) should get a
    # short, natural reply instead of being forced into the structured
    # troubleshooting template. Only treat it as a greeting when the
    # WHOLE message is casual small talk, not just a message that
    # contains "hi" as a substring of a real question.
    if question in GREETING_PHRASES:
        return "greeting"

    for keyword in TROUBLESHOOTING_KEYWORDS:
        if _contains_phrase(question, keyword):
            return "troubleshooting"

    for keyword in LAB_KEYWORDS:
        if _contains_phrase(question, keyword):
            return "lab_help"

    return "general"