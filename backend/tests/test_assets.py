from fastapi.testclient import TestClient
from app.api.routes import app
from app.api.services.favorite_service import (
    FavoriteRepository,
    get_favorite_repository,
)
from app.core.repositories.favorite_repositorie import FavoriteRepository
from app.db.config import get_session
from app.core.models.favorite_models import FavoritesCrypto


client = TestClient(app)
session = next(get_session())
favorite_repository = FavoriteRepository(FavoritesCrypto, session)
service = get_favorite_repository(favorite_repository=favorite_repository)


def test_add_favorite():
    # Test add a favorite
    favorite_input = FavoritesCrypto(symbol="BTC")
    headers = {"Authorization": "Bearer your_access_token"}

    response = client.post("/add_favorite", json=favorite_input, headers=headers)

    assert response.status_code == 200
    assert response.json() == {"message": "Ok"}


def test_remove_favorite():
    # Test removing a favorite
    symbol = "BTC"
    headers = {"Authorization": "Bearer your_access_token"}

    response = client.post(
        "/remove_favorite", params={"symbol": symbol}, headers=headers
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Ok"}


def test_show_favorites():
    # Test showing favorites
    headers = {"Authorization": "Bearer your_access_token"}
    response = client.get("/show_favorites", headers=headers)

    assert response.status_code == 200
