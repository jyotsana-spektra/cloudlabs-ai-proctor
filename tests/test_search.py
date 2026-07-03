import requests

BASE_URL = "http://localhost:8000"


def test_search():
    response = requests.get(f"{BASE_URL}/health")

    assert response.status_code == 200
