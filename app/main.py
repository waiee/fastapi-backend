from fastapi import FastAPI
from pydantic import BaseModel
from gradio_client import Client
import json

app = FastAPI()
client = Client("anasmarz/penat")

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

@app.post("/submit")
async def submit_form(request: PredictRequest):
    # Call the /lambda endpoint
    lambda_response = client.predict(api_name="/lambda")

    # Call the /predict endpoint with parameters from the request
    predict_response = client.predict(
        request.market_sector,
        request.target_market,
        request.revenue_stream,
        request.budget,
        request.technology_used,
        request.temperature,
        request.max_new_tokens,
        request.top_p,
        request.repetition_penalty,
        api_name="/predict"
    )

    # Call the /cleanup endpoint
    cleanup_response = client.predict(api_name="/cleanup")

    # Prepare the JSON response
    response = {
        "lambda_response": lambda_response,
        "predict_response": predict_response,
        "cleanup_response": cleanup_response
    }
    return json.loads(json.dumps(response))
