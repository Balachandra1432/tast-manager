from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    class Config:
        orm_mode = True

class TaskCreate(BaseModel):
    title: str
    description: Optional[str]
    status: Optional[str] = "pending"
    deadline: Optional[datetime]
    user_id: int

class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    deadline: Optional[datetime]
    assigned_user: UserOut
    class Config:
        from_attributes = True