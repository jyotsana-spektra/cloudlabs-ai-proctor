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


# Phrases that mean the learner is explicitly asking to be connected to a
# human/CloudLabs support, regardless of whether they also described a lab
# issue. Checked directly against the learner's own message, independent of
# how the AI ends up answering, so escalation intent is never missed just
# because the model's reply happens not to use certain wording.
SUPPORT_REQUEST_PHRASES = [
    "connect me to support",
    "connect me with support",
    "connect to support",
    "connect me to cloudlabs support",
    "talk to a human",
    "talk to support",
    "talk to a person",
    "talk to someone",
    "speak to a human",
    "speak with a human",
    "speak to support",
    "speak to someone",
    "human agent",
    "human support",
    "real person",
    "live agent",
    "live chat",
    "escalate",
    "raise a ticket",
    "open a ticket",
    "file a ticket",
    "contact support",
    "contact cloudlabs",
    "reach support",
    "reach out to support",
    "get me support",
    "need a human",
    "need human help",
    "customer support",
    "support team",
]


def wants_human_support(question: str) -> bool:
    """True when the learner's own message is asking to be connected to a
    human/support channel, e.g. "connect me to support" or "I want to talk
    to a human" -- independent of lab-issue keywords or the AI's answer."""

    question = question.lower().strip()
    return any(phrase in question for phrase in SUPPORT_REQUEST_PHRASES)


# Patterns for requests that ask Brainy to actually PERFORM an
# administrative/account/environment action on the learner's behalf --
# extend a lab's duration, unlock an account, issue a refund, grant admin
# access, etc. Brainy is a chat copilot with no real access to make these
# changes, so these should go straight to a "can't do that, contact
# support" answer instead of the AI guessing, hallucinating a workaround,
# or asking an unhelpful clarifying question. Kept separate from
# TROUBLESHOOTING_KEYWORDS/LAB_KEYWORDS since this is about the *type of
# ask* (do this FOR me) rather than a topic.
ACTION_REQUEST_PATTERNS = [
    r"\bextend\b.{0,30}\b(lab|duration|time|session|deadline|access)\b",
    r"\b(add|give|grant)\b.{0,15}\bmore time\b",
    r"\bmore time\b.{0,15}\b(lab|session|exercise)\b",
    r"\breset\b.{0,20}\b(vm|lab|environment|timer)\b.{0,15}\bfor me\b",
    r"\bunlock\b.{0,20}\b(account|lab|vm|environment)\b",
    r"\b(grant|give)\b.{0,15}\b(admin|administrator)\b.{0,15}\baccess\b",
    r"\bdelete\b.{0,15}\baccount\b",
    r"\brefund\b",
    r"\bcancel\b.{0,15}\b(subscription|order|license|licence)\b",
    r"\b(upgrade|downgrade)\b.{0,15}\b(plan|subscription|license|licence)\b",
    r"\brenew\b.{0,15}\b(license|licence|subscription)\b",
    r"\brestart\b.{0,20}\benvironment\b.{0,15}\bfor me\b",
]


def wants_unavailable_action(question: str) -> bool:
    """True when the learner is asking Brainy to directly perform an
    account/environment/admin action (e.g. "can you extend my lab
    duration?") rather than asking for information or troubleshooting
    help. Brainy has no real access to do these, so they should be routed
    straight to CloudLabs Support instead of answered/clarified."""

    question = question.lower().strip()
    return any(re.search(pattern, question) for pattern in ACTION_REQUEST_PATTERNS)


# Patterns for messages that look like an attempt to abuse/misuse the lab
# environment rather than a genuine lab question -- e.g. spinning up extra
# resources beyond what the lab assigned, trying to get Brainy to ignore
# its own instructions, or other clearly malicious intent (credential
# theft, attacking other systems, etc.). These should never be answered
# normally: Brainy should refuse and flag the session for the CloudLabs
# support/proctor team to review, since this is a policy-violation signal
# rather than something the AI should try to help with.
RESOURCE_MISUSE_PATTERNS = [
    r"\b(create|spin up|provision|deploy|launch)\b.{0,20}\b(extra|additional|another|more|multiple|unlimited)\b.{0,20}\b(vm|vms|virtual machine|machines|resource|resources|subscription|subscriptions)\b",
    r"\b(extra|additional|unlimited)\b.{0,15}\b(vm|vms|resources|credits)\b",
    r"\bcreate\b.{0,15}\b(another|a new|extra)\b.{0,15}\bsubscription\b",
    r"\bbypass\b.{0,20}\b(quota|limit|restriction)\b",
    r"\b(increase|remove|get around)\b.{0,15}\bquota\b",
    r"\bfree\b.{0,10}\bazure\b.{0,10}\bcredit\b",
    r"\b(mine|mining)\b.{0,15}\b(crypto|cryptocurrency|bitcoin|ethereum)\b",
    r"\buse\b.{0,20}\b(this|the)\b.{0,15}\blab\b.{0,20}\bfor\b.{0,20}\b(personal|my own|side)\b.{0,15}\bproject\b",
    r"\bkeep\b.{0,15}\b(this|the)\b.{0,15}\b(vm|environment|resources|subscription)\b.{0,20}\bafter\b.{0,15}\blab\b.{0,15}\bends\b",
]

MISCHIEF_PATTERNS = [
    r"\bignore\b.{0,20}\b(previous|prior|all|your)\b.{0,15}\binstructions\b",
    r"\bignore\b.{0,15}\byour\b.{0,15}\brules\b",
    r"\bjailbreak\b",
    r"\bpretend\b.{0,15}\byou\b.{0,15}\bare\b",
    r"\bact as\b.{0,15}\b(dan|unrestricted|jailbroken)\b",
    r"\bhack\b.{0,20}\b(into|the|another)\b",
    r"\bexploit\b.{0,20}\b(vulnerability|system|environment|vm)\b",
    r"\b(ddos|denial of service)\b",
    r"\b(brute[\s-]?force)\b.{0,15}\bpassword\b",
    r"\bsql injection\b",
    r"\b(steal|share|sell)\b.{0,15}\b(credential|password|login)\b",
    r"\baccess\b.{0,20}\b(another|someone else|other)\b.{0,15}\b(student|user|account|environment|lab)\b",
    r"\bunauthorized access\b",
    r"\bcrack\b.{0,15}\bpassword\b",
    r"\b(malware|ransomware|phishing)\b",
    r"\battack\b.{0,20}\b(another|other|external)\b.{0,15}\b(system|server|network|site)\b",
]

MISUSE_PATTERNS = RESOURCE_MISUSE_PATTERNS + MISCHIEF_PATTERNS


def detects_misuse(question: str) -> bool:
    """True when the learner's message looks like an attempt to misuse the
    lab environment (e.g. provisioning extra/unauthorized resources, crypto
    mining, bypassing quotas) or other clearly malicious intent (prompt
    injection / jailbreak attempts, credential theft, attacking other
    systems). This is independent of question_type -- Brainy should never
    try to help with these, and the session should be flagged for the
    CloudLabs support/proctor team to review instead."""

    question = question.lower().strip()
    return any(re.search(pattern, question) for pattern in MISUSE_PATTERNS)