from app.core.repositories.favorite_repositorie import FavoriteRepository, get_favorite_repository
from typing import Type
from sqlalchemy.exc import NoResultFound
from app.core.models.favorite_models import FavoritesCrypto
from app.api.services.base import Service 
from fastapi import Depends



class FavoriteService(Service):
    def __init__(self, repository: FavoriteRepository):
         super().__init__(repository)

    def create_favorite(self,symbol: str, user_id: int ) -> FavoritesCrypto:
          favorite = self.repository.create_favorite_repository(symbol=symbol,user_id=user_id)
          return favorite
    
    def create_favorite_on_db(self, favorite: Type[FavoritesCrypto]) -> FavoritesCrypto:
         self.repository.create_favorite_on_db_repository(favorite=favorite)

    def remove_favorite_on_db(self,user_id: int, symbol: str) -> FavoritesCrypto:
         self.repository.remove_favorite_on_db_repository(user_id=user_id,symbol=symbol)
       
    def get_all_favorites(self,user_id: int) -> dict:
         favorites = self.repository.get_all_favorites_on_db_repository(user_id=user_id)
         favorite_list = [{'id': favorite.id, 'symbol': favorite.symbol} for favorite in favorites]
         return {'id': user_id, 'favorites': favorite_list  }
    

def get_favorite_repository(favorite_repository: FavoriteRepository = Depends(get_favorite_repository)):
    return FavoriteService(repository=favorite_repository)