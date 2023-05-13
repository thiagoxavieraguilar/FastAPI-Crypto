from .config import engine
from app.core.models.base import Base

async def creat_database():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all())
        await connection.run_sync(Base.metadata.creat_all())

