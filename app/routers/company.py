from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas, dependencies
from app.dependencies import get_db
from gradio_client import Client
import json
import logging

router = APIRouter()

logging.basicConfig(level=logging.INFO)

@router.post("/predict_and_create_company", response_model=schemas.GradioOutput)
async def predict_and_create_company(
    company: schemas.CompanyCreate,
    db: Session = Depends(get_db)
):
    try:
        # Store company details in the database
        created_company = crud.create_company(db=db, company=company)

        # Extract the necessary parameters for Gradio
        gradio_params = {
            "market_sector": company.sector,
            "target_market": company.target_market,
            "revenue_stream": company.revenue_stream,
            "budget": company.budget,
            "technology_used": company.technology,
            "temperature": 0.9,
            "max_new_tokens": 256,
            "top_p": 0.9,
            "repetition_penalty": 1.2
        }

        # Pass company details to Gradio for processing
        gradio_client = Client("anasmarz/penat")
        gradio_output = gradio_client.predict(**gradio_params, api_name="/predict")

        # Print the output from Gradio
        logging.info("Output from Gradio:")
        logging.info(gradio_output)

        # Return the output as a string
        return {"output": gradio_output}

    except Exception as e:
        logging.error(f"Error in predict_and_create_company: {e}")
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

@router.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logging.error(f"Validation error: {exc}")
    return JSONResponse(
        status_code=422,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )
