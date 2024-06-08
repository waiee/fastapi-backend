# from pydantic import BaseModel

# class CompanyBase(BaseModel):
#     sector: str
#     target_market: str
#     revenue_stream: str
#     budget: str
#     technology: str

# class CompanyCreate(CompanyBase):
#     name: str
#     location: str
#     established_year: int
#     description: str

# class CompanyUpdate(CompanyBase):
#     pass

# class Company(CompanyBase):
#     id: int

#     class Config:
#         orm_mode: True

# class GradioOutput(BaseModel):
#     output: str

#     class Config:
#         orm_mode = True

from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"  # Update with your database URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

class Investor(Base):
    __tablename__ = "investors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)
    locations = Column(String)
    markets = Column(Text)
    past_investments = Column(Text)
    profile_url = Column(String)

Base.metadata.create_all(bind=engine)

from pydantic import BaseModel

class InvestorCreate(BaseModel):
    name: str
    type: str
    locations: str
    markets: str
    past_investments: str
    profile_url: str

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/investors/", response_model=InvestorCreate)
def create_investor(investor: InvestorCreate, db: Session = Depends(get_db)):
    db_investor = Investor(**investor.dict())
    db.add(db_investor)
    db.commit()
    db.refresh(db_investor)
    return db_investor

@app.get("/investors/{investor_id}", response_model=InvestorCreate)
def read_investor(investor_id: int, db: Session = Depends(get_db)):
    db_investor = db.query(Investor).filter(Investor.id == investor_id).first()
    if db_investor is None:
        raise HTTPException(status_code=404, detail="Investor not found")
    return db_investor
