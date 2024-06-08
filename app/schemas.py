from pydantic import BaseModel
from typing import Optional

class CompanyBase(BaseModel):
    name: str
    sector: str
    location: str
    established_year: int
    description: Optional[str] = None

class CompanyCreate(CompanyBase):
    pass

class CompanyUpdate(CompanyBase):
    name: Optional[str] = None
    sector: Optional[str] = None
    location: Optional[str] = None
    established_year: Optional[int] = None
    description: Optional[str] = None

class Company(CompanyBase):
    id: int

    class Config:
        from_attributes = True
