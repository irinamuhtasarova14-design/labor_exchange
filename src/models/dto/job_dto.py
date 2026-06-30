from decimal import Decimal
from typing import Optional
import datetime
from bases.base_dto import BaseDTO

class JobCreateDTO(BaseDTO):
    title: str
    description: str
    salary_from: Optional[Decimal] = None
    salary_to: Optional[Decimal] = None
    is_active: bool = True

class JobDTO(BaseDTO):
    id: int
    user_id: int
    title: str
    description: str
    salary_from: Optional[Decimal]
    salary_to: Optional[Decimal]
    is_active: bool
    created_at: datetime.datetime

class JobUpdateDTO(BaseDTO):
    title: Optional[str] = None
    description: Optional[str] = None
    salary_from: Optional[Decimal] = None
    salary_to: Optional[Decimal] = None
    is_active: Optional[bool] = None