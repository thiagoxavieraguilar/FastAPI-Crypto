from fastapi.testclient import TestClient
from app.api.routes import app
from app.api.services.user_service import get_user_service, UserService
from app.core.repositories.user_repositorie import UserRepository
from fastapi import Depends
from app.db.config import get_session
from app.core.models.user_models import User


client = TestClient(app)
session = next(get_session())
user_repository = UserRepository(User, session)
service = get_user_service(user_repository=user_repository)


def test_create_user_success():
    # Test create user
    user_input = {"username": "new_user", "password": "password"}

    response = client.post("user/create_user", json=user_input)
    user_db = service.get_username(username=user_input["username"])

    assert response.status_code == 200
    assert response.json() == {"message": "Ok user created"}
    assert user_db.username == user_input["username"]


def test_create_user_failed():
    # Test data with a username its already exist
    user_input = {"username": "user_exist", "password": "password"}

    response = client.post("user/create_user", json=user_input)

    assert response.status_code == 400


def test_login_sucess():
    # Test successful login
    form_data = {
        "username": "tx",
        "password": "tx",
        "grant_type": "password",
    }

    response = client.post(
        "user/login",
        data=form_data,
        headers={"content-type": "application/x-www-form-urlencoded"},
    )

    assert response.status_code == 200
    assert response.json().get("access_token") is not None
    assert response.json().get("token_type") == "bearer"


def test_login_failed():
    # Test login with incorrect password

    form_data = {
        "username": "tx",
        "password": "wrong_password",
        "grant_type": "password",
    }

    response = client.post(
        "user/login",
        data=form_data,
        headers={"content-type": "application/x-www-form-urlencoded"},
    )

    assert response.status_code == 400
    assert response.json().get("access_token") == None
    assert response.json().get("token_type") == None
