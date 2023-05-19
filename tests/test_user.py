from fastapi.testclient import TestClient
from app.api.routes import app
from app.api.services.user_service import get_user_service,UserService
from fastapi import Depends




client = TestClient(app)

def test_read_root():
    response = client.get("user/home")
    assert response.status_code == 200





