from app.core.repositories.user_repositorie import UserRepository,get_user_repository
from typing import List, Optional, Tuple, Type
from sqlalchemy.exc import NoResultFound
from app.core.models.user_models import User  
from app.api.services.base import Service 
from fastapi import Depends,HTTPException
from datetime import datetime, timedelta
from jose import jwt, JWTError
from werkzeug.security import check_password_hash,generate_password_hash
import os
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from fastapi import status


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

load_dotenv()
SECRET_KEY = os.environ.get('SECRET_KEY')
ALGORITHM = os.environ.get('ALGORITHM')


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

    def get_username(self, username: str) -> User:
          return self.repository.get_username_repository(username=username) 

    def validate_password(self,input_password: str , hashed_password: str):
         return check_password_hash(hashed_password, input_password)
          

    def create_access_token(self,username: str, expire_in: int = 30) -> jwt:
        exp = datetime.utcnow() + timedelta(minutes=expire_in)
        payload = {
            'sub': username,
            'exp': exp
        }
        
        access_token = jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
        
        return {
            'access_token': access_token,
            'exp': exp.isoformat()
        }
    
    def verify_token(self, access_token: dict) -> User:
        try:
            data = jwt.decode(access_token, SECRET_KEY, algorithm=[ALGORITHM])

            print(data['sub'])
            user_on_db = self.get_username(username=data['sub'])
            print(user_on_db.username)
            if user_on_db is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail='Invalid access token'
                )
            
            return user_on_db.username

        except jwt.DecodeError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid access token'
            )
def get_user_service(user_repository: UserRepository = Depends(get_user_repository)):
    return UserService(repository=user_repository)








