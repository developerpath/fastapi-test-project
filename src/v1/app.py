from fastapi import FastAPI
from .routers import pokemon, utils

app = FastAPI(title="Pokemon REST API")

app.include_router(pokemon.router, tags=["Pokemon"])
app.include_router(utils.router, tags=["Utilities"])
