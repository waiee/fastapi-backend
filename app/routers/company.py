from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas, dependencies
from app.dependencies import SessionLocal
from gradio_client import Client
from app.schemas import PredictionResult
import json

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/companies/", response_model=schemas.Company)
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    return crud.create_company(db=db, company=company)

@router.get("/companies/", response_model=List[schemas.Company])
def read_companies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    companies = crud.get_companies(db, skip=skip, limit=limit)
    return companies

@router.get("/companies/{company_id}", response_model=schemas.Company)
def read_company(company_id: int, db: Session = Depends(get_db)):
    db_company = crud.get_company(db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company

@router.put("/companies/{company_id}", response_model=schemas.Company)
def update_company(company_id: int, company: schemas.CompanyUpdate, db: Session = Depends(get_db)):
    db_company = crud.get_company(db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return crud.update_company(db=db, company_id=company_id, company_update=company)

@router.delete("/companies/{company_id}", response_model=schemas.Company)
def delete_company(company_id: int, db: Session = Depends(get_db)):
    db_company = crud.get_company(db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return crud.delete_company(db=db, company_id=company_id)

@router.post("/predict", response_model=PredictionResult)
async def predict_from_gradio(
    market_sector: str,
    target_market: str,
    revenue_stream: str,
    budget: str,
    technology_used: str,
    temperature: float = 0.9,
    max_new_tokens: int = 2048,
    top_p: float = 0.9,
    repetition_penalty: float = 1.2
):
    # Pass company details to Gradio for processing
    gradio_client = Client("anasmarz/penat")
    gradio_output = gradio_client.predict(
        market_sector=market_sector,
        target_market=target_market,
        revenue_stream=revenue_stream,
        budget=budget,
        technology_used=technology_used,
        temperature=temperature,
        max_new_tokens=max_new_tokens,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        api_name="/predict"
    )
    
    # Log Gradio output for debugging
    print("Gradio output:", gradio_output)
    
    # Try to parse the Gradio output from string to JSON
    try:
        gradio_output_json = json.loads(gradio_output)
    except json.JSONDecodeError:
        print("Gradio output is not valid JSON:", gradio_output)
        raise HTTPException(status_code=500, detail="Failed to parse Gradio output")

    # Validate the Gradio output JSON in FastAPI Swagger
    required_fields = ["market_sector", "target_market", "revenue_stream", "budget", "technology_used", "temperature", "max_new_tokens", "top_p", "repetition_penalty"]
    missing_fields = [field for field in required_fields if field not in gradio_output_json]
    
    if missing_fields:
        print("Gradio output is missing required fields:", missing_fields)
        raise HTTPException(status_code=500, detail=f"Gradio output is missing required fields: {missing_fields}")

    return gradio_output_json
