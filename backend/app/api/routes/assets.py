from fastapi import APIRouter, Depends, HTTPException
from app.api.services.favorite_service import FavoriteService, get_favorite_repository
from typing import List
from app.api.schemas.favorite_input_schema import FavoriteInput
from app.api.schemas.message_schema import StandardOutput, ErrorOutput
from app.api.schemas.price_favorite_schema import PriceFavorite
from fastapi import Depends
from app.api.services.depends import token_verifier
from app.api.services.asset_service import AssetService, get_assets_service
from asyncio import gather

assets = APIRouter(prefix="/assets", dependencies=[Depends(token_verifier)])


@assets.post(
    "/add_favorite",
    description="My description",
    response_model=StandardOutput,
    responses={400: {"model": ErrorOutput}},
)
async def create_user(
    favorite_input: FavoriteInput,
    currentUser=Depends(token_verifier),
    service: FavoriteService = Depends(get_favorite_repository),
):
    try:
        user_id = currentUser["id"]
        favorite = service.create_favorite(
            symbol=favorite_input.symbol.upper(), user_id=user_id
        )
        service.create_favorite_on_db(favorite=favorite)
        return StandardOutput(message="Ok")
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@assets.post(
    "/remove_favorite",
    description="My description",
    response_model=StandardOutput,
    responses={400: {"model": ErrorOutput}},
)
async def remove_favorite(
    symbol: str,
    currentUser=Depends(token_verifier),
    service: FavoriteService = Depends(get_favorite_repository),
):
    try:
        user_id = currentUser["id"]
        service.remove_favorite_on_db(user_id=user_id, symbol=symbol)
        return StandardOutput(message="Ok")
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@assets.get(
    "/show_favorites",
    description="My description",
    response_model=List[PriceFavorite],
    responses={400: {"model": ErrorOutput}},
)
async def remove_favorite(
    currentUser=Depends(token_verifier),
    service: FavoriteService = Depends(get_favorite_repository),
    asset_service: AssetService = Depends(get_assets_service),
):
    try:
        user_id = currentUser["id"]
        response_data = service.get_all_favorites(user_id=user_id)
        favorites = response_data["favorites"]
        print([favorite["symbol"] for favorite in favorites])
        tasks = [
            asset_service.get_price(symbol=favorite["symbol"]) for favorite in favorites
        ]
        return await gather(*tasks)
    except Exception as error:
        raise HTTPException(400, detail=str(error))
