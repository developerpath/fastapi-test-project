from fastapi import FastAPI
from src.v1.routers import health_check, pokemon

app = FastAPI(title="Pokemon REST API")

app.include_router(pokemon.router, tags=["Pokemon"])
app.include_router(health_check.router, tags=["Utilities"])
