from pydantic import BaseModel, EmailStr
from typing import Optional
from models.enums import UserRole

class UserDTO(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: UserRole

class UserCreateDTO(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: UserRole

class UserUpdateDTO(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[UserRole] = None