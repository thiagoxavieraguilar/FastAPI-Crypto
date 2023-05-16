from app.core.repositories.user_repositorie import UserRepository,get_user_repository
from typing import List, Optional, Tuple, Type
from sqlalchemy.exc import NoResultFound
from app.core.models.user_models import User  
from app.api.services.base import Service 
from fastapi import Depends
from werkzeug.security import generate_password_hash


class UserService(Service):
    def __init__(self, repository: UserRepository):
         super().__init__(repository)

    def create_user(self, username: str, password: str) -> User:
         hashed_password = generate_password_hash(password, method='scrypt')
         user =  self.repository.create_user_repository(username=username, password=hashed_password)
         return user
    
    def create_user_on_db(self,user:Type[User]) -> User:
          self.repository.create_user_on_db_repository(user)

    def delete_user_on_db(self,user_id: int) -> User:
          self.repository.delete_user_on_db_repository(user_id)


def get_user_service(user_repository: UserRepository = Depends(get_user_repository)):
    return UserService(repository=user_repository)