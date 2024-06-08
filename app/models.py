from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    sector = Column(String, index=True)
    location = Column(String, index=True)
    established_year = Column(Integer, index=True)
    description = Column(String, index=True)
