from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.models.user_models import User 
from app.db.config import get_session

from .base import BaseRepository
from typing  import  Type
from werkzeug.security import check_password_hash


class UserRepository(BaseRepository):
    """User Repository is an interface to the database."""

    def get_username_repository(self, username: str) -> User:
        return self.query().filter_by(username=username).one()

    def create_user_repository(self,username: str, password: str) -> User:
        return User(username=username,password=password) 

    def create_user_on_db_repository(self,user: Type[User]) -> User:
        self.create(user)


    def delete_user_on_db_repository (self,user_id: int) -> None:
        self.delete(user_id)

    def validate_password_repository(self, input_password: str , hashed_password: str):
        return check_password_hash(hashed_password, input_password)
         

    
def get_user_repository(db: Session = Depends(get_session)) -> UserRepository:
    return UserRepository(User, db)