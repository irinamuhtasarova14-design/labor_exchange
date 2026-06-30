from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
from datetime import datetime

class JobDTO(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    salary_from: Optional[Decimal]
    salary_to: Optional[Decimal]
    is_active: bool
    created_at: datetime

class JobCreateDTO(BaseModel):
    title: str
    description: str
    salary_from: Optional[Decimal] = None
    salary_to: Optional[Decimal] = None
    is_active: bool = True

class JobUpdateDTO(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    salary_from: Optional[Decimal] = None
    salary_to: Optional[Decimal] = None
    is_active: Optional[bool] = None