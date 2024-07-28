from fastapi import APIRouter, HTTPException
from v1.schemas.common import HealthCheckResponse

router = APIRouter()

@router.get("/healthz", response_model=HealthCheckResponse)
async def health_check():
    try:
        content = HealthCheckResponse(message="OK", status=200)
        return content
    except Exception as e:
        detail = [i.strip() for i in str(e).split('\n')]
        raise HTTPException(status_code=500, detail=detail)
