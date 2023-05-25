from fastapi.testclient import TestClient
from app.api.routes import app
from app.api.services.favorite_service import FavoriteRepository,get_favorite_repository
from app.core.repositories.favorite_repositorie import FavoriteRepository
from app.db.config import get_session
from app.core.models.favorite_models import FavoritesCrypto


client = TestClient(app)
session = next(get_session())
favorite_repository = FavoriteRepository(FavoritesCrypto,session)
service = get_favorite_repository(favorite_repository=favorite_repository)


# Test create_user function
def test_create_user():
    response = client.post('/add_favorite', json={'symbol': 'BTC'},  params={'currentUser': 1})
   
    assert response.status_code == 200
    assert response.json() == {'message': 'Ok'}




def test_show_favorites():
    # Test case 1: Successful retrieval of favorites
    response = client.get('/show_favorites')
    assert response.status_code == 200