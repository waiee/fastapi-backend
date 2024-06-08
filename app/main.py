from fastapi import FastAPI
from app.routers import company

app = FastAPI()

app.include_router(company.router, prefix="/companies", tags=["companies"])
