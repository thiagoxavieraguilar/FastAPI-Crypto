from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from app.db.config import get_session
from sqlalchemy.orm import Session
from app.api.services.user_service import UserService
from app.api.services.user_service import get_user_service

oauth_scheme = OAuth2PasswordBearer(tokenUrl='/user/login')



def token_verifier(service: UserService = Depends(get_user_service), token = Depends(oauth_scheme)):
    service.verify_token(access_token=token)