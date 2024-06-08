# import re
# import requests

# # Define the backend URL
# backend_url = "http://127.0.0.1:8000"

# def call_predict(market_sector, target_market, revenue_stream, budget, technology_used, temperature, max_new_tokens, top_p, repetition_penalty):
#     payload = {
#         "market_sector": market_sector,
#         "target_market": target_market,
#         "revenue_stream": revenue_stream,
#         "budget": budget,
#         "technology_used": technology_used,
#         "temperature": temperature,
#         "max_new_tokens": max_new_tokens,
#         "top_p": top_p,
#         "repetition_penalty": repetition_penalty
#     }
#     response = requests.post(f"{backend_url}/predict", json=payload)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Error: {response.status_code}")
#         print(response.text)
#         return None

# def extract_phases(predict_response):
#     if 'predict_response' in predict_response:
#         # Extract the predict response text
#         predict_text = predict_response['predict_response']
        
#         # Define the regex pattern to match the phases and quarters
#         pattern = r"\*\*Phase \d: [^\n]+\*\*|\*\*Quarter \d: [^\n]+\*\*"
        
#         # Find all matches
#         matches = re.findall(pattern, predict_text)
        
#         # Split the text by the matches
#         split_text = re.split(pattern, predict_text)[1:]
        
#         # Combine the matches and split text into a dictionary
#         phases = {}
#         for match, text in zip(matches, split_text):
#             phases[match.strip()] = text.strip()
        
#         return phases
#     else:
#         print("Error: 'predict_response' key not found in the response")
#         return {}

# # Example usage
# predict_response = call_predict(
#     market_sector="Fintech",
#     target_market="SMEs",
#     revenue_stream="Subscription Based Service",
#     budget="RM20000",
#     technology_used="solana, rust",
#     temperature=0.9,
#     max_new_tokens=3008,
#     top_p=0.9,
#     repetition_penalty=1.2
# )

# if predict_response:
#     phases = extract_phases(predict_response)

#     # Print the separated phases
#     # for phase, content in phases.items():
#     #     print(f"{phase}\n{content}\n")

#     # Print the keys and values in the phases dictionary
#     for phase, content in phases.items():
#         print(f"Key: {phase}")
#         print(f"Value: {content}\n")

##########################################

import re
import requests

# Define the backend URL
backend_url = "http://127.0.0.1:8000"

def call_predict(market_sector, target_market, revenue_stream, budget, technology_used, temperature, max_new_tokens, top_p, repetition_penalty):
    payload = {
        "market_sector": market_sector,
        "target_market": target_market,
        "revenue_stream": revenue_stream,
        "budget": budget,
        "technology_used": technology_used,
        "temperature": temperature,
        "max_new_tokens": max_new_tokens,
        "top_p": top_p,
        "repetition_penalty": repetition_penalty
    }
    response = requests.post(f"{backend_url}/predict", json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

def extract_phases(predict_response):
    if 'predict_response' in predict_response:
        # Extract the predict response text
        predict_text = predict_response['predict_response']
        
        # Define the regex pattern to match the phases and quarters
        pattern = r"\*\*(Phase \d: [^\n]+|\bQuarter \d: [^\n]+)\*\*"
        
        # Find all matches
        matches = re.findall(pattern, predict_text)
        
        # Split the text by the matches
        split_text = re.split(pattern, predict_text)[1:]
        
        # Combine the matches and split text into a list of dictionaries
        roadmap = []
        for match, text in zip(matches, split_text):
            phase = {
                "phaseTitle": match.strip(),
                "goals": extract_section("Goal", text),
                "goalDetails": extract_section_details("Goal", text),
                "keyActivities": extract_section_details("Key Activities & Initiatives", text),
                "resourceAllocation": extract_section_details("Resource Allocation", text),
                "risks": extract_section_details("Risks & Mitigations", text, False),
                "kpis": extract_section_details("Key Performance Indicators (KPIs)", text)
            }
            roadmap.append(phase)
        
        return roadmap
    else:
        print("Error: 'predict_response' key not found in the response")
        return []

def extract_section(header, text):
    pattern = rf"\*{header}\*:([^\n]+)"
    match = re.search(pattern, text)
    if match:
        return match.group(1).strip()
    return ""

def extract_section_details(header, text, split_lines=True):
    pattern = rf"\*\*{header}\*\*:\n([^\*]+)"
    match = re.search(pattern, text)
    if match:
        details = match.group(1).strip()
        if split_lines:
            return [detail.strip() for detail in details.split('\n') if detail.strip()]
        else:
            return details
    return []

# Example usage
predict_response = call_predict(
    market_sector="Fintech",
    target_market="SMEs",
    revenue_stream="Subscription Based Service",
    budget="RM20000",
    technology_used="solana, rust",
    temperature=0.9,
    max_new_tokens=2800,
    top_p=0.9,
    repetition_penalty=1.2
)
print(predict_response)

if predict_response:
    roadmap = extract_phases(predict_response)

    # Print the structured roadmap
    for phase in roadmap:
        print(phase)

##########################################
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from gradio_client import Client
# import re

# app = FastAPI()

# client = Client("anasmarz/penat")

# class PredictRequest(BaseModel):
#     market_sector: str
#     target_market: str
#     revenue_stream: str
#     budget: str
#     technology_used: str
#     temperature: float
#     max_new_tokens: int
#     top_p: float
#     repetition_penalty: float

# @app.post("/predict")
# def call_predict(request: PredictRequest):
#     try:
#         predict_response = client.predict(
#             market_sector=request.market_sector,
#             target_market=request.target_market,
#             revenue_stream=request.revenue_stream,
#             budget=request.budget,
#             technology_used=request.technology_used,
#             temperature=request.temperature,
#             max_new_tokens=request.max_new_tokens,
#             top_p=request.top_p,
#             repetition_penalty=request.repetition_penalty,
#             api_name="/predict"
#         )
#         predict_text = predict_response['predict_response']
#         pattern = r"\*\*Phase \d: [^\n]+\*\*|\*\*Quarter \d: [^\n]+\*\*"
#         matches = re.findall(pattern, predict_text)
#         split_text = re.split(pattern, predict_text)[1:]
#         phases = {match.strip(): text.strip() for match, text in zip(matches, split_text)}
#         return {"phases": phases}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

