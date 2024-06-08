from pydantic import BaseModel

class CompanyBase(BaseModel):
    name: str
    description: str
    sector: str
    target_market: str
    revenue_stream: str
    budget: str
    technology: str
    location: str
    established_year: str

class CompanyCreate(CompanyBase):
    pass

class CompanyUpdate(CompanyBase):
    pass

class Company(CompanyBase):
    id: int

    class Config:
        orm_mode: True

class GradioOutput(BaseModel):
    output: str  # Assuming the Gradio output is a string, adjust based on actual output structure

    class Config:
        orm_mode = True
