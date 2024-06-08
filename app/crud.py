from sqlalchemy.orm import Session
from app import models, schemas

def create_company(db: Session, company: schemas.CompanyCreate):
    db_company = models.Company(
        name=company.name,
        sector=company.sector,
        location=company.location,
        established_year=company.established_year,
        description=company.description
    )
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

def get_companies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Company).offset(skip).limit(limit).all()

def get_company(db: Session, company_id: int):
    return db.query(models.Company).filter(models.Company.id == company_id).first()

def update_company(db: Session, company_id: int, company_update: schemas.CompanyUpdate):
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if not db_company:
        return None
    for key, value in company_update.dict(exclude_unset=True).items():
        setattr(db_company, key, value)
    db.commit()
    db.refresh(db_company)
    return db_company

def delete_company(db: Session, company_id: int):
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if db_company:
        db.delete(db_company)
        db.commit()
    return db_company
