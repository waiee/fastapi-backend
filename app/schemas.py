from pydantic import BaseModel
from typing import Optional

class CompanyBase(BaseModel):
    name: str
    sector: str
    location: str
    established_year: int
    description: Optional[str] = None
    target_market: Optional[str] = None   # New field
    technology: Optional[str] = None      # New field
    revenue_stream: Optional[str] = None  # New field

class CompanyCreate(CompanyBase):
    pass

class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    sector: Optional[str] = None
    location: Optional[str] = None
    established_year: Optional[int] = None
    description: Optional[str] = None
    target_market: Optional[str] = None   # New field
    technology: Optional[str] = None      # New field
    revenue_stream: Optional[str] = None  # New field

class Company(CompanyBase):
    id: int

    class Config:
        orm_mode = True
