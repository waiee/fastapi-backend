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
    budget: int

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
    budget: Optional[int] = None

class Company(CompanyBase):
    id: int

    class Config:
        orm_mode = True

class PredictionResult(BaseModel):
    market_sector: str
    target_market: str
    revenue_stream: str
    budget: str
    technology_used: str
    temperature: float
    max_new_tokens: int
    top_p: float
    repetition_penalty: float

