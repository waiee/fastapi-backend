from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from gradio_client import Client

app = FastAPI()

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List

DATABASE_URL = "sqlite:///./test.db"  # Update with your database URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

class Investor(Base):
    __tablename__ = "investors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)
    locations = Column(String)
    markets = Column(Text)
    past_investments = Column(Text)
    profile_url = Column(String)

Base.metadata.create_all(bind=engine)

class InvestorCreate(BaseModel):
    name: str
    type: str
    locations: str
    markets: str
    past_investments: str
    profile_url: str

class InvestorRead(BaseModel):
    id: int
    name: str
    type: str
    locations: str
    markets: str
    past_investments: str
    profile_url: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/investors/", response_model=InvestorCreate)
def create_investor(investor: InvestorCreate, db: Session = Depends(get_db)):
    db_investor = Investor(**investor.dict())
    db.add(db_investor)
    db.commit()
    db.refresh(db_investor)
    return db_investor

@app.get("/investors/{investor_id}", response_model=InvestorRead)
def read_investor(investor_id: int, db: Session = Depends(get_db)):
    db_investor = db.query(Investor).filter(Investor.id == investor_id).first()
    if db_investor is None:
        raise HTTPException(status_code=404, detail="Investor not found")
    return db_investor

@app.get("/investors/sector/{sector}", response_model=List[InvestorRead])
def read_investors_by_sector(sector: str, db: Session = Depends(get_db)):
    db_investors = db.query(Investor).filter(Investor.markets.like(f"%{sector}%")).all()
    if not db_investors:
        raise HTTPException(status_code=404, detail="No investors found for this sector")
    return db_investors



# Initialize the client with the app name
client = Client("anasmarz/penat")

# Define the request model for the /predict endpoint
class PredictRequest(BaseModel):
    market_sector: str
    target_market: str
    revenue_stream: str
    budget: str
    technology_used: str
    temperature: float
    max_new_tokens: int
    top_p: float
    repetition_penalty: float

@app.get("/lambda")
def call_lambda():
    try:
        lambda_response = client.predict(api_name="/lambda")
        return {"lambda_response": lambda_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict")
def call_predict(request: PredictRequest):
    try:
        predict_response = client.predict(
            market_sector=request.market_sector,
            target_market=request.target_market,
            revenue_stream=request.revenue_stream,
            budget=request.budget,
            technology_used=request.technology_used,
            temperature=request.temperature,
            max_new_tokens=request.max_new_tokens,
            top_p=request.top_p,
            repetition_penalty=request.repetition_penalty,
            api_name="/predict"
        )
        
        return {"predict_response": predict_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/cleanup")
def call_cleanup():
    try:
        cleanup_response = client.predict(api_name="/cleanup")
        return {"cleanup_response": cleanup_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#### fetch

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict

app = FastAPI()

# Allow CORS for your frontend URL (e.g., http://localhost:3000 for Next.js dev environment)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

data = {
    '*Phase 1 – Q1 & Q2 (Initial Setup):': {
        'Key Activities & Initiatives:': '\n1. Set up company operations, HR processes, financial systems, and legal structures\n2. Conduct SWOT analysis, Porter’s Five Forces analysis, and competitive landscape assessment\n3. Develop value proposition, minimum viable product (MVP), and business plan\n4. Recruit founders, board members, advisors, and key personnel, focusing on those experienced in blockchain, Solana, Rust, and fintech industries\n5. Establish relationships with local authorities, regulatory bodies, and industry associations\n',
        'Resource Allocation:': '\n1. Hire legal, accounting, and recruitment services\n2. Allocate budget towards market research tools and analytics software\n3. Secure office space or coworking space for the team\n4. Allocate funds towards registration fees, insurance premiums, and licensing costs\n',
        'Risk Management:': '\n1. Identify risks related to regulations, competition, technological changes, talent acquisition, and financial stability\n2. Implement risk management strategies such as regular compliance checks, diversifying the product offering, investing in continuous learning programs, building strong networks, maintaining cash reserves, and seeking strategic partnerships when needed\n',
        'KPIs & Metrics:': '\n1. Successful incorporation of the business\n2. Completion of market research and identification of target customer segments\n3. Formulation of an acceptable business plan and value proposition\n4. Adequate staffing levels achieved for key positions\n5. Registered as compliant with all relevant laws and regulations'
    },
    'Phase 2 – Q3 (Develop Main Features & Functionality):': {
        'Key Activities & Initiatives:': '\n1. Design the architecture and user interface/user experience (UI/UX) of the product\n2. Integrate APIs from third-party service providers if required (e.g., payment gateways, banks, etc.)\n3. Develop smart contracts for various transactions and implement them on the Solana blockchain network\n4. Test the product thoroughly through internal testing, user acceptance testing (UAT), and external beta testing\n5. Optimize the product for speed, efficiency, and user friendliness\n6. Gather feedback from testers and make improvements accordingly\n',
        'Resource Allocation:': '\n1. Recruit additional developers skilled in Solana, Rust, and other necessary programming languages\n2. Invest in hardware infrastructure suitable for hosting the application and running the Solana nodes\n3. Purchase development tools, libraries, and frameworks to accelerate the process\n4. Engage quality assurance specialists to ensure high standards are maintained throughout the development process\n',
        'Risk Management:': '\n1. Ensure adherence to best practices and industry standards in coding and design, as well as cybersecurity measures to protect sensitive data\n2. Address potential compatibility issues with existing third-party solutions during integration\n',
        'KPIs & Metrics:': '\n1. Progress on the development timeline\n2. Quality of the final product as assessed by users\n3. Number of bugs encountered and resolved\n4. Efficiency of the product, measured in terms of transaction processing times and resource usage'
    },
    'Phase 3 – Q4 (Deployment & Launch):*': {
        'Key Activities & Initiatives:': '\n1. Finalize marketing materials, content strategy, and go-to-market strategy\n2. Partner with strategic organizations, payment gateway providers, and banks to facilitate smooth adoption among merchants\n3. Train customer support representatives and account managers\n4. Launch the product at a press event, inviting media, investors, partners, and influencers\n5. Onboard early adopter merchants and provide personalized support to help them adapt quickly\n6. Collect feedback from these early adopters, identify common issues, and iterate upon the product to fix any problems and add requested features\n7. Expand the user base gradually but steadily, engaging in targeted advertising and networking efforts to attract more merchants\n',
        'Resource Allocation:': '\n1. Increase headcount in customer support, sales, and marketing teams\n2. Invest in public relations agencies to maximize visibility\n3. Advertise on platforms frequented by merchants and small businesses\n4. Attend industry events, conferences, and trade shows to expand the brand presence and generate leads\n',
        'Risk Management:': '\n1. Monitor ongoing performance closely, making adjustments as needed to maintain growth momentum\n2. Continuously engage with stakeholders to keep them informed about updates, milestones, and challenges faced by the startup\n3. Evaluate competitors regularly, identifying opportunities to differentiate further\n',
        'KPIs & Metrics:': '\n1. Growth rate in active merchants using the platform\n2. Customer satisfaction ratings (Net Promoter Score [NPS] and overall sentiment analysis)\n3. Sales conversion rates from lead generation activities\n4. Operational expenses compared to revenue generated</s>'
    }
}

@app.get("/data", response_model=Dict)
async def get_data():
    return data

@app.get("/", tags=["Root"])
async def hello():
    return {"hello": "anjing la vercel"}

