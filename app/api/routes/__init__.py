from app.api.routes.user import user_router
from app.api.routes.assets import assets
from fastapi import FastAPI

app = FastAPI()
app.include_router(user_router)
app.include_router(assets)