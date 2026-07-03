from backend.services.classifier_service import classify_question


def test_vm_issue():
    assert classify_question("VM is not loading") == "troubleshooting"


def test_lab_question():
    assert classify_question("How do I create a Lakehouse?") == "lab_help"


def test_general_question():
    assert classify_question("Hello") == "general"