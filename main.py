import uvicorn
from app.db import create_database
from app.api.routes import app

if __name__ == "__main__":
    create_database()
    uvicorn.run(app, host="0.0.0.0", port=8000)
