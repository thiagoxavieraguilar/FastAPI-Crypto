from app.api.routes import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_root():
    response = client.get("user/home")
    assert response.status_code == 200




def test_create_user():
    user_input = {"username": "test_user", "password": "test_password"}
    response = client.post("/user/create_user", json=user_input)
    assert response.status_code == 200
    assert response.json() == "test_user"