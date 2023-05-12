from db.config import engine
from .base import Base
from asyncio import run


async def creat_database():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all())
        await connection.run_sync(Base.metadata.creat_all())

if __name__=="__main__":
    run(creat_database())