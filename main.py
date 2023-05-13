from app.api.routes.hello import app
import uvicorn
from asyncio import run
from app.db.init_db import creat_database

if __name__ == "__main__":
    
    uvicorn.run(app, host="localhost", port=8000)
    run(creat_database())