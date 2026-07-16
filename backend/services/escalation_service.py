from datetime import datetime

escalation_store = []

# Separate store for auto-flagged alerts (resource misuse / mischief
# detected straight from the learner's message -- see
# classifier_service.detects_misuse). Kept separate from escalation_store
# so genuine "please help" escalations aren't mixed in with policy-violation
# alerts the support/proctor team needs to review with priority.
flagged_alerts = []


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


def flag_misuse(
    session_id: str,
    user_message: str,
    reason: str,
    lab_context: dict | None = None,
):
    """Records an auto-detected misuse/mischief attempt (e.g. trying to
    provision extra resources, jailbreak attempts, credential theft) so the
    CloudLabs support/proctor team can review it. This is the "alert
    support" mechanism for these cases -- there is no outbound
    email/webhook integration configured, so flagged alerts are surfaced
    via GET /admin/alerts instead."""

    alert = {
        "timestamp": datetime.utcnow().isoformat(),
        "session_id": session_id,
        "user_message": user_message,
        "reason": reason,
        "lab_context": lab_context or {},
        "severity": "high",
    }

    flagged_alerts.append(alert)

    return alert


def get_flagged_alerts():
    return flagged_alerts