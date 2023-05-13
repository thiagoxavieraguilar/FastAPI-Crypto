from fastapi import FastAPI
from fastapi import APIRouter, Depends, HTTPException, Response, status
from app.api.services.user_service import UserService, get_user_service
from app.api.schemas.user_schema import UserInput
from fastapi import Depends

import uvicorn

app = FastAPI()
'''
@app.post('/home')
async def create_user(user_input = UserInput, service: UserService = Depends(get_user_service)):
    return service.create_user(username=user_input.username, password=user_input.password)

'''

@app.post('/home')
async def create_user(username : str, password: str, service= Depends(get_user_service)):
    return service.create_user(username=username, password=password)
