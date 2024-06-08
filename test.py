import requests

API_URL = "http://127.0.0.1:8000/investors/"

def get_input(prompt):
    return input(prompt).strip()

def main():
    print("Enter Investor Details")
    name = get_input("Name: ")
    type_ = get_input("Type: ")
    locations = get_input("Locations: ")
    markets = get_input("Markets (comma-separated): ")
    past_investments = get_input("Past Investments (comma-separated): ")
    profile_url = get_input("Profile URL: ")

    investor_data = {
        "name": name,
        "type": type_,
        "locations": locations,
        "markets": markets,
        "past_investments": past_investments,
        "profile_url": profile_url
    }

    response = requests.post(API_URL, json=investor_data)
    if response.status_code == 200:
        print("Investor added successfully!")
        print(response.json())
    else:
        print("Error adding investor:", response.status_code, response.text)

if __name__ == "__main__":
    main()
