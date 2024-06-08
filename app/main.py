from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from gradio_client import Client

app = FastAPI()

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
