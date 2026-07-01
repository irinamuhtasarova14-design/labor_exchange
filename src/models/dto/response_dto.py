from typing import Optional
import datetime
from bases.base_dto import BaseDTO
from models.enums import ResponseStatus

class ResponseDTO(BaseDTO):
    id: int
    job_id: int
    user_id: int
    message: Optional[str]
    status: ResponseStatus
    created_at: datetime.datetime

class ResponseCreateDTO(BaseDTO):
    job_id: int
    message: Optional[str] = None

class ResponseUpdateDTO(BaseDTO):
    status: Optional[ResponseStatus] = None
    message: Optional[str] = None