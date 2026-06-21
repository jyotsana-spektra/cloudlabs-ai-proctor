def classify_question(question: str) -> str:
    question = question.lower()

    troubleshooting_keywords = [
        "error", "issue", "failed", "failure", "cannot", "can't",
        "unable", "stuck", "not working", "not loading",
        "unavailable", "access denied", "permission", "vm", "rdp",
        "deployment failed", "button not visible"
    ]

    lab_help_keywords = [
        "how", "create", "configure", "setup", "where",
        "what step", "which option", "task", "exercise",
        "workspace", "lakehouse", "eventhouse", "ontology"
    ]

    if any(keyword in question for keyword in troubleshooting_keywords):
        return "troubleshooting"

    if any(keyword in question for keyword in lab_help_keywords):
        return "lab_help"
