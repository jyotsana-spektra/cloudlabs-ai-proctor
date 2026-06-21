def classify_question(question: str) -> str:

    question = question.lower()

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