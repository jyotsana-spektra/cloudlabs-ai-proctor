import requests

BASE_URL = "http://localhost:8000"


def test_feedback():
    payload = {
        "session_id": "test-session",
        "user_message": "VM is not loading",
        "answer": "Wait a few minutes.",
        "rating": 1
    }

    response = requests.post(f"{BASE_URL}/feedback/", json=payload)

    assert response.status_code == 200
