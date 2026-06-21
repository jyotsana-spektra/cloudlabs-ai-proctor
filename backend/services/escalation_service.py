escalation_store = []


def save_escalation(
    session_id: str,
    issue_summary: str,
    lab_id: str | None = None,
    lab_name: str | None = None,
    exercise: str | None = None,
    task: str | None = None,
    step: str | None = None
):
    escalation = {
        "session_id": session_id,
        "issue_summary": issue_summary,
        "lab_id": lab_id,
        "lab_name": lab_name,
        "exercise": exercise,
        "task": task,
        "step": step
    }

    escalation_store.append(escalation)

    return {
        "success": True,
        "message": "Diagnostic issue captured successfully.",
        "data": escalation
    }


def get_escalations():
    return escalation_store