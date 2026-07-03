import requests

BASE_URL = "http://localhost:8000"


def test_create_escalation():
    payload = {
        "session_id": "test-session",
        "issue_summary": "User is unable to load the VM.",
        "lab_id": "fabric",
        "lab_name": "Fabric IQ",
        "exercise": "Exercise 2",
        "task": "Task 3",
        "step": "Step 5"
    }

    response = requests.post(f"{BASE_URL}/escalate/", json=payload)

    assert response.status_code == 200


def test_list_escalations():
    response = requests.get(f"{BASE_URL}/escalate/")

    assert response.status_code == 200