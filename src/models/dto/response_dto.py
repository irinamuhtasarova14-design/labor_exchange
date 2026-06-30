from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from models.enums import ResponseStatus

class ResponseDTO(BaseModel):
    id: int
    job_id: int
    user_id: int
    message: Optional[str]
    status: ResponseStatus
    created_at: datetime

class ResponseCreateDTO(BaseModel):
    job_id: int
    message: Optional[str] = None

class ResponseUpdateDTO(BaseModel):
    status: Optional[str] = None
    message: Optional[str] = None