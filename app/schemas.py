from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    email: str
    password: str

class UserCreate(UserBase):
    pass

class UserUpdateSensitive(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None

class UserUpdateNonSensitive(BaseModel):
    company_name: Optional[str] = None
    company_sector: Optional[str] = None
    location: Optional[str] = None
    established_year: Optional[int] = None
    description: Optional[str] = None

class User(UserBase):
    id: int
    username: Optional[str] = None
    company_name: Optional[str] = None
    company_sector: Optional[str] = None
    location: Optional[str] = None
    established_year: Optional[int] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True
