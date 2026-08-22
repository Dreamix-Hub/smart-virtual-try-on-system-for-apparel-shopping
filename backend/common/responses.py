from typing import TypeVar, Generic

from pydantic import BaseModel

T = TypeVar("T")

class SuccessResponse(BaseModel, Generic[T]):
    status: bool = True
    data: T

class ErrorDetail(BaseModel):
    code: str
    message: str
    
class ErrorResponse(BaseModel):
    status: bool = False
    error: ErrorDetail