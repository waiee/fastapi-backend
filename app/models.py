from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    # New fields
    company_name = Column(String, nullable=True)
    company_sector = Column(String, nullable=True)
    location = Column(String, nullable=True)
    established_year = Column(Integer, nullable=True)
    description = Column(String, nullable=True)

Base.metadata.create_all(engine)


