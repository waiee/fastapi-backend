# from gradio_client import Client
import json

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

# # Split the output text by "---" to separate each phase
# phases = predict_response.split("---")

# result_dict = {}

# # Iterate over each phase
# for phase in phases:
#     # Split the phase into lines
#     lines = phase.strip().split("\n")
    
#     # Extract the phase title
#     phase_title = lines[0].strip()
    
#     # Initialize a dictionary to store the content within each section
#     section_dict = {}
    
#     # Initialize variables to track the current section title and content
#     current_section_title = None
#     current_section_content = []
    
#     # Iterate over the lines starting from the second line
#     for line in lines[1:]:
#         # Check if the line starts with "" indicating the start of a new section
#         if line.strip().startswith(""):
#             # If current_section_title is not None, add it to section_dict
#             if current_section_title is not None:
#                 section_dict[current_section_title] = "\n".join(current_section_content)
            
#             # Extract the section title from the line
#             current_section_title = line.strip().strip("")
            
#             # Initialize an empty list for the new section content
#             current_section_content = []
#         else:
#             # Append the line to the current section content
#             current_section_content.append(line.strip())
    
#     # Add the last section to section_dict
#     if current_section_title is not None:
#         section_dict[current_section_title] = "\n".join(current_section_content)
    
#     # Add the section_dict to the result dictionary with the phase title as key
#     result_dict[phase_title] = section_dict

# # Print the result dictionary
# print(result_dict)

# for i, j in result_dict.items():
#     print(i)
#     x=0
#     for key in j:
#         x=x+1
#         print(x)
#         print(key)
#         print("---------------------\n",j[key])

import json

dict_data = {
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

# Write the dictionary to a JSON file
with open("my.json", "w") as f:
    json.dump(dict_data, f, indent=4)

# Read and print the JSON file
with open("my.json", "r") as f:
    parsed = json.load(f)
    print(json.dumps(parsed, indent=4))
