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
