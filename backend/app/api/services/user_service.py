from app.core.repositories.user_repositorie import UserRepository, get_user_repository
from typing import Type
from app.core.models.user_models import User
from app.api.services.base import Service
from fastapi import Depends, Depends, status, HTTPException
from datetime import datetime, timedelta
from jose import jwt, JWTError
import os
from dotenv import load_dotenv
from passlib.context import CryptContext
from fastapi.responses import JSONResponse


pwd_context = CryptContext(schemes=["sha256_crypt"])


load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")


class UserService(Service):
    def __init__(self, repository: UserRepository):
        super().__init__(repository)

    def create_user(self, username: str, password: str) -> User:
        hashed_password = pwd_context.hash(password)
        user = self.repository.create_user_repository(
            username=username, password=hashed_password
        )
        return user

    def create_user_on_db(self, user: Type[User]) -> User:
        self.repository.create_user_on_db_repository(user)

    def delete_user_on_db(self, user_id: int) -> User:
        self.repository.delete_user_on_db_repository(user_id)

    def get_username(self, username: str) -> User:
        return self.repository.get_username_repository(username=username)

    def validate_password(self, input_password: str, hashed_password: str):
        return pwd_context.verify(input_password, hashed_password)

    def create_access_token(self, username: str, expire_in: int = 30) -> dict:
        exp = datetime.utcnow() + timedelta(minutes=expire_in)
        payload = {"sub": username, "exp": exp}

        access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

        return access_token

    def verify_token(self, access_token: str) -> dict:
        try:
            payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
            username = str(payload.get("sub"))

            user_on_db = self.get_username(username=username)

            if user_on_db is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid access token",
                )

            payload = {"username": username, "id": user_on_db.id}
            return payload
        except JWTError:
            return JSONResponse(
                content={"message": "Invalid token"},
                status_code=status.HTTP_401_UNAUTHORIZED,
            )


def get_user_service(user_repository: UserRepository = Depends(get_user_repository)):
    return UserService(repository=user_repository)
