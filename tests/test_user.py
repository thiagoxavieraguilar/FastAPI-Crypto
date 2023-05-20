from fastapi.testclient import TestClient
from app.api.routes import app
from app.api.services.user_service import get_user_service,UserService
from app.core.repositories.user_repositorie import UserRepository
from fastapi import Depends
from app.db.config import get_session
from app.core.models.user_models import User
from werkzeug.security import check_password_hash


client = TestClient(app)
session = next(get_session())
user_repository = UserRepository(User,session)
service = get_user_service(user_repository=user_repository)


def test_login():
    username = 'tx'
    password = 'tx'

    user_db = service.get_username(username=username)
    
    # Send a POST request to the login endpoint
    response = client.post("user/login",json={"username": username, "password": password})

    # Verify the response status code
    assert response.status_code == 200

    # Verify the response body
    assert response.json() == {"message": "Ok logado"}

    # Verify the username adn password

    assert user_db.username == username
    assert check_password_hash(user_db.password, password)


def test_login_failure():
    non_existing_username = 'tx'
    incorrect_password = 'wrongpassword'

    # Send a POST request to the login endpoint with incorrect username and password
    response = client.post("user/login", json={"username": non_existing_username, "password": incorrect_password})

    # Verify the response status code
    assert response.status_code == 401

    # Verify the response body
    assert response.json() == {"detail": "Incorrect username or password"}
