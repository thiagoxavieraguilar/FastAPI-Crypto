from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.models.user_models import User 
from app.db.config import get_session

from .base import BaseRepository
from typing  import  Type


class UserRepository(BaseRepository):
    """User Repository is an interface to the database."""

    def get_username(self, username: str) -> User:
        return self.query().filter_by(username=username).one()

    def create_user_repository(self,username: str, password: str) -> User:
        return User(username=username,password=password) 

    def create_user_on_db(self, user: Type[User]) -> User:
        return self.create(user)

def get_user_repository(db: Session = Depends(get_session)) -> UserRepository:
    return UserRepository(User, db)