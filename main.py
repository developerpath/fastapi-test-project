from fastapi import FastAPI
from config import settings
from app_v1.main import app as app_v1

app = FastAPI(title=settings.app_name, openapi_url=None)

app.mount("/v1", app_v1)
