from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"name": "Naveen", "email": "naveen@example.com"})
    assert response.status_code == 200
    assert response.json()["email"] == "naveen@example.com"

def test_create_task():
    client.post("/users/", json={"name": "Test", "email": "test@example.com"})
    response = client.post("/tasks/", json={
        "title": "Test Task",
        "description": "Test Description",
        "status": "pending",
        "deadline": None,
        "user_id": 1
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"