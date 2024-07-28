# import json
from fastapi import APIRouter

# from src.models.book_models_v1 import Book

router = APIRouter()


@router.get("/healthz")
async def health_check_v1():
    return {"message": "Ok", "status": 200}
