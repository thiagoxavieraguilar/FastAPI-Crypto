from fastapi import FastAPI
from fastapi import APIRouter, Depends, HTTPException, Response, status
from app.api.services.user_service import UserService, get_user_service
from app.api.schemas.user_schema import UserInput
from fastapi import Depends

user_router = APIRouter(prefix='/user')



@user_router.post('/create_user')
async def create_user(user_input: UserInput, service: UserService = Depends(get_user_service)):
    user = await service.create_user(username=user_input.username, password=user_input.password)
    return user.username



@user_router.get('/home')
async def home():
    return "ok"