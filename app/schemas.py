from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str
    company_name: str
    company_sector: str
    location: str
    established_year: int
    description: str

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
    company_name: Optional[str] = None
    company_sector: Optional[str] = None
    location: Optional[str] = None
    established_year: Optional[int] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True
