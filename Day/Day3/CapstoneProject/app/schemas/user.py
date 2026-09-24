#define the Pydantic models that the FastAPI uses to
#validate incoming request bodies
#shapes the outgoing response

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from app.models.user import UserRole

class UserCreate(BaseModel):
    name:str = Field(...,min_length=2, max_length=100, description="Full name of the user")
    email:EmailStr = Field(...,description="unique email address, used as login identifier")
    password:str = Field(...,min_length=8,description="Password of the user")
    role: UserRole = Field(default=UserRole.EMPLOYEE, description="one of:employee,support_engineer,team_lead,admin")

class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    role: UserRole
    created_at: datetime

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[str] = None
