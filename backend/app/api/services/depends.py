from fastapi import Depends, HTTPException,status
from app.api.services.user_service import UserService
from app.api.services.user_service import get_user_service

from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer


oauth_scheme = OAuth2PasswordBearer(tokenUrl='/user/login')

def token_verifier(token = Depends(oauth_scheme),service: UserService = Depends(get_user_service)):
    return service.verify_token(access_token=token)


