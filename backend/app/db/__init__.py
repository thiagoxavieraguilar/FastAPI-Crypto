from .config import engine
from app.core.models.base import Base
from app.core.models.favorite_models import FavoritesCrypto
from app.core.models.user_models import User


def create_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
