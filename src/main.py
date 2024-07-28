from fastapi import FastAPI
from v1.app import app as app_v1

app = FastAPI(title="Pokemon REST API", openapi_url=None)

app.mount("/v1", app_v1)

