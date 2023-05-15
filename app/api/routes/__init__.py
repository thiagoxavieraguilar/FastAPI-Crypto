from app.api.routes.user import user_router
from fastapi import FastAPI

app = FastAPI()
app.include_router(user_router)