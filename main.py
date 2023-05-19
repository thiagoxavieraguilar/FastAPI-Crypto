import uvicorn
from app.db import create_database
from app.api.routes import app

if __name__ == "__main__":
    create_database()
    uvicorn.run(app, host="localhost", port=8000)
