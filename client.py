# import requests

# # Define the backend URL
# backend_url = "http://127.0.0.1:8000"

# def call_lambda():
#     response = requests.get(f"{backend_url}/lambda")
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Error: {response.status_code}")
#         print(response.text)

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

# def call_cleanup():
#     response = requests.get(f"{backend_url}/cleanup")
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Error: {response.status_code}")
#         print(response.text)

# # Example usage
# lambda_response = call_lambda()
# print("Lambda Response:", lambda_response)

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
# print("Predict Response:", predict_response)

# cleanup_response = call_cleanup()
# print("Cleanup Response:", cleanup_response)

import re
import requests

# Define the backend URL
backend_url = "http://127.0.0.1:8000"

def call_lambda():
    response = requests.get(f"{backend_url}/lambda")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

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

def call_cleanup():
    response = requests.get(f"{backend_url}/cleanup")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

def extract_phases(predict_response):
    if 'predict_response' in predict_response:
        # Use regex to find all occurrences of text between '**'
        phases = re.findall(r'\*\* (.*?)\*\*', predict_response['predict_response'])
        return phases
    else:
        print("Error: 'predict_response' key not found in the response")
        return []

# Example usage
lambda_response = call_lambda()
print("Lambda Response:", lambda_response)

predict_response = call_predict(
    market_sector="Fintech",
    target_market="SMEs",
    revenue_stream="Subscription Based Service",
    budget="RM20000",
    technology_used="solana, rust",
    temperature=0.9,
    max_new_tokens=3008,
    top_p=0.9,
    repetition_penalty=1.2
)
print("Predict Response:", predict_response)

# Extract the predict response text
predict_text = predict_response['predict_response']

# Define the regex pattern to match the phases and quarters
pattern = r"\*\*Phase \d: [^\n]+\*\*|\*\*Quarter \d: [^\n]+\*\*"

# Find all matches
matches = re.findall(pattern, predict_text)

# Split the text by the matches
split_text = re.split(pattern, predict_text)[1:]

# Combine the matches and split text into a dictionary
phases = {}
for match, text in zip(matches, split_text):
    phases[match.strip()] = text.strip()

# Print the separated phases
for phase, content in phases.items():
    print(f"{phase}\n{content}\n")

# If needed, you can convert the dictionary to a structured format (e.g., JSON) for further use
# import json
# phases_json = json.dumps(phases, indent=2)
# print(phases_json)
