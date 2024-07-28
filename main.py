from fastapi import FastAPI
from app_v1.main import app as app_v1

app = FastAPI(title="Pokemon REST API", openapi_url=None)

app.mount("/v1", app_v1)
