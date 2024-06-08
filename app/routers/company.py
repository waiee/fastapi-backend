from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas, dependencies
from app.dependencies import SessionLocal
from gradio_client import Client
import json

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@@router.post("/predict_and_create_company", response_model=schemas.GradioOutput)
async def predict_and_create_company(
    company: schemas.CompanyCreate,
    db: Session = Depends(get_db)
):
    # Store company details in the database
    created_company = crud.create_company(db=db, company=company)

    # Extract the necessary parameters for Gradio
    gradio_params = {
        "market_sector": company.sector,
        "target_market": company.target_market,
        "revenue_stream": company.revenue_stream,
        "budget": company.budget,
        "technology_used": company.technology,
        "established_year": company.established_year,  # Pass established_year to Gradio
        "temperature": 0.9,
        "max_new_tokens": 2048,
        "top_p": 0.9,
        "repetition_penalty": 1.2
    }

    try:
        # Pass company details to Gradio for processing
        gradio_client = Client("anasmarz/penat")
        gradio_output = gradio_client.predict(**gradio_params, api_name="/predict")

        # Try to parse the Gradio output from string to JSON
        try:
            gradio_output_json = json.loads(gradio_output)
        except json.JSONDecodeError as e:
            raise HTTPException(status_code=500, detail=f"Failed to parse Gradio output: {e}")

        # Validate the Gradio output JSON in FastAPI Swagger
        required_fields = ["market_sector", "target_market", "revenue_stream", "budget", "technology_used"]
        missing_fields = [field for field in required_fields if field not in gradio_output_json]

        if missing_fields:
            raise HTTPException(status_code=500, detail=f"Gradio output is missing required fields: {missing_fields}")

        # Return the Gradio output as a validated JSON structure
        return gradio_output_json

    except Exception as e:
        print(f"Error in predict_and_create_company: {e}")
        raise HTTPException(status_code=500, detail="Failed to process Gradio output")

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
