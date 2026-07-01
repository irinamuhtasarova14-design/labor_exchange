from typing import Optional
from bases.base_dto import BaseDTO
import datetime
from models.enums import UserRole

class UserCreateDTO(BaseDTO):
    email: str
    name: str
    password: str
    role: UserRole

class UserDTO(BaseDTO):
    id: int
    email: str
    name: str
    hashed_password: str
    role: UserRole
    created_at: datetime.datetime

class UserUpdateDTO(BaseDTO):
    email: Optional[str] = None
    name: Optional[str] = None
    hashed_password: Optional[str] = None
    role: Optional[UserRole] = None