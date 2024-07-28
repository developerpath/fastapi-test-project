from pydantic import BaseModel
from enum import Enum

class BoolStr(str, Enum):
    true = "true"
    false = "false"

class ErrorResponse(BaseModel):
    detail: str
    status_code: int
