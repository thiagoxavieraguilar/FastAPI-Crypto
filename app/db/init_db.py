from .config import engine
from app.core.models.base import Base

def create_database():
    Base.metadata.create_all(bind=engine)
