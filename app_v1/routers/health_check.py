from fastapi import APIRouter, HTTPException
from app_v1.schemas.common import HealthCheckResponse

router = APIRouter()


@router.get("/healthz", response_model=HealthCheckResponse)
def health_check():
    try:
        content = HealthCheckResponse(message="OK", status=200)
        return content
    except Exception:
        raise HTTPException(status_code=500)
