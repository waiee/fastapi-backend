from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    sector = Column(String, index=True)
    location = Column(String, index=True)
    established_year = Column(Integer, index=True)
    description = Column(String, index=True)
    target_market = Column(String, index=True)  # New field
    technology = Column(String, index=True)     
    revenue_stream = Column(String, index=True)
    budget = Column(Integer, index=True)   

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
