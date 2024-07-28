from pydantic import BaseModel, NonNegativeInt
from enum import Enum

class BoolStr(str, Enum):
    true = "true"
    false = "false"

class HealthCheckResponse(BaseModel):
    message: str
    status: NonNegativeInt
