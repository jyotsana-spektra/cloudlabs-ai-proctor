import requests

BASE_URL = "http://localhost:8000"


def test_escalation():
    payload = {
        "session_id": "test-session",
        "reason": "Low confidence response"
    }

    response = requests.post(f"{BASE_URL}/escalate", json=payload)

    assert response.status_code in [200, 404]
