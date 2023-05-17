from fastapi import FastAPI
from fastapi import APIRouter, Depends, HTTPException, Response, status
from app.api.services.favorite_service import FavoriteService, get_favorite_repository
from app.api.schemas.favorite_schema import FavoriteInput
from app.api.schemas.message_schema import StandardOutput, ErrorOutput
from fastapi import Depends

assets = APIRouter(prefix='/assets')


@assets.post('/add_favorite', description='My description', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def create_user(favorite_input: FavoriteInput, service: FavoriteService = Depends(get_favorite_repository)):
    try:
        favorite = service.create_favorite(symbol=favorite_input.symbol.upper(), quantity=favorite_input.quantity, user_id=favorite_input.user_id)
        service.create_favorite_on_db(favorite=favorite)
        return StandardOutput(message='Ok') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@assets.post('/remove_favorite', description='My description', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def create_user(user_id: str, symbol: str, service: FavoriteService = Depends(get_favorite_repository)):
    try:
        service.remove_favorite_on_db(user_id=user_id,symbol=symbol)
        return StandardOutput(message='Ok') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))