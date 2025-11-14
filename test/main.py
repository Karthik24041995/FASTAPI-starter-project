from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}

def test_create_and_list_user():
    user_data = {"name": "John", "email": "john@example.com"}
    resp = client.post("/users/", json=user_data)
    assert resp.status_code == 200
    user = resp.json()
    assert user["id"] == 1
    assert user["name"] == "John"
    assert user["email"] == "john@example.com"

    get_resp = client.get("/users/")
    assert get_resp.status_code == 200
    users = get_resp.json()
    assert any(u["email"] == "john@example.com" for u in users)
