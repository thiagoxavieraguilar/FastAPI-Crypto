from fastapi import APIRouter, Depends, HTTPException
from app.api.services.favorite_service import FavoriteService, get_favorite_repository
from app.api.schemas.favorite_schema import FavoriteInput
from app.api.schemas.message_schema import StandardOutput, ErrorOutput
from fastapi import Depends
from app.api.services.depends import token_verifier
from fastapi.responses import JSONResponse

assets = APIRouter(prefix='/assets',dependencies=[Depends(token_verifier)])


@assets.post('/add_favorite', description='My description', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def create_user(favorite_input: FavoriteInput, currentUser = Depends(token_verifier), service: FavoriteService = Depends(get_favorite_repository)):
    try:
        user_id = currentUser['id']
        favorite = service.create_favorite(symbol=favorite_input.symbol.upper(), quantity=favorite_input.quantity, user_id=user_id)
        service.create_favorite_on_db(favorite=favorite)
        return StandardOutput(message='Ok') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@assets.post('/remove_favorite', description='My description', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def remove_favorite(symbol: str, currentUser = Depends(token_verifier), service: FavoriteService = Depends(get_favorite_repository)):
    try:
        user_id = currentUser['id']
        service.remove_favorite_on_db(user_id=user_id,symbol=symbol)
        return StandardOutput(message='Ok') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    

@assets.get('/show_favorites', description='My description', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def remove_favorite(currentUser = Depends(token_verifier), service: FavoriteService = Depends(get_favorite_repository)):
    try:
        user_id = currentUser['id']
        response_data = service.get_all_favorites(user_id=user_id)
        return JSONResponse(content=response_data)
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    
