# from gradio_client import Client

# # Initialize the client with the app name
# client = Client("anasmarz/penat")

# # Call the /lambda endpoint (assuming no parameters are needed)
# lambda_response = client.predict(
#     api_name="/lambda"
# )
# print("Lambda Response:", lambda_response)

# # Call the /predict endpoint with the specified parameters
# predict_response = client.predict(
#     market_sector="Fintech",  # market_sector
#     target_market="Merchant",  # target_market
#     revenue_stream="Product",  # revenue_stream
#     budget="RM30000",  # budget
#     technology_used="solana, rust",  # technology_used
#     temperature=0.9,  # temperature
#     max_new_tokens=3008,  # max_new_tokens
#     top_p=0.9,  # top_p
#     repetition_penalty=1.2,  # repetition_penalty
#     api_name="/predict"  # api_name
# )
# print("Predict Response:", predict_response)

# # Call the /cleanup endpoint (assuming no parameters are needed)
# cleanup_response = client.predict(
#     api_name="/cleanup"
# )
# print("Cleanup Response:", cleanup_response)