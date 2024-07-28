from fastapi import FastAPI
from config import settings
from app_v1.routers import health_check, pokemon

app = FastAPI(title=settings.app_name)

app.include_router(pokemon.router, tags=["Pokemon"])
app.include_router(health_check.router, tags=["Utilities"])
