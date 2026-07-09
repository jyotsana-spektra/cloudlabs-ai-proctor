GREETING_PHRASES = {
    "hi", "hii", "hiii", "hello", "hey", "heyy", "yo",
    "good morning", "good afternoon", "good evening",
    "thanks", "thank you", "thx", "ty",
    "bye", "goodbye", "see you", "ok", "okay", "cool", "great", "nice",
}


def classify_question(question: str) -> str:

    question = question.lower().strip().strip(".,!?")

    # Casual chit-chat (greetings/thanks/acknowledgements) should get a
    # short, natural reply instead of being forced into the structured
    # troubleshooting template. Only treat it as a greeting when the
    # WHOLE message is casual small talk, not just a message that
    # contains "hi" as a substring of a real question.
    if question in GREETING_PHRASES:
        return "greeting"

    troubleshooting_keywords = [
        "error",
        "failed",
        "failure",
        "issue",
        "problem",
        "cannot",
        "can't",
        "stuck",
        "login",
        "denied",
        "timeout",
        "loading",
        "vm",
        "browser"
    ]

    lab_keywords = [
        "exercise",
        "task",
        "step",
        "workspace",
        "lakehouse",
        "eventhouse",
        "ontology",
        "agent",
        "fabric"
    ]

    for keyword in troubleshooting_keywords:
        if keyword in question:
            return "troubleshooting"

    for keyword in lab_keywords:
        if keyword in question:
            return "lab_help"

    return "general"