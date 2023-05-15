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

    async def create_user(self, username: str, password: str) -> User:
         hashed_password = generate_password_hash(password, method='scrypt')
         user = await self.repository.create_user_repository(username=username, password=hashed_password)
         self.create_user_on_db(user=user)
         return user
    
    def create_user_on_db(self,user:Type[User]) -> User:
          return  self.repository.create_user_on_db_repository(user)


def get_user_service(user_repository: UserRepository = Depends(get_user_repository)):
    return UserService(repository=user_repository)