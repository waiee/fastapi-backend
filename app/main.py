from fastapi import FastAPI
from app.routers import company, gradio
from app.dependencies import engine
from app.models import Base

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(company.router)
app.include_router(company.router, prefix="/companies", tags=["companies"])
app.include_router(gradio.router) 
