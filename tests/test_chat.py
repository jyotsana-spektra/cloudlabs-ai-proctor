import requests

BASE_URL = "http://localhost:8000"


def test_chat():
    payload = {
        "session_id": "test-session",
        "user_message": "VM is not loading",
        "lab_id": "fabric",
        "lab_name": "Fabric IQ",
        "exercise": "Exercise 2",
        "task": "Task 3",
        "step": "Step 5"
    }

    response = requests.post(f"{BASE_URL}/chat", json=payload)

    assert response.status_code == 200
    assert "answer" in response.json()
