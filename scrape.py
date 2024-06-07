import requests
from bs4 import BeautifulSoup

# URL and base URL
URL = "https://angelmatch.io/investors/by-market/software/malaysia"
base_url = "https://angelmatch.io/"

# User input for the market
user_market = input("Enter the market you are interested in: ").strip().lower()

# Request the page
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# Find all investor elements
elements = soup.find_all(class_='investors_details__yykj9')

# Extract href values and store investor data
investors_data = []
href_values = [element.get('href') for element in elements]

# Iterate through href values to process each investor
for href in href_values:
    if href:
        full_url = base_url + href
        response = requests.get(full_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            investor_card = soup.find('div', class_='investors_investorPageWrapper__5r7zg')
            
            if investor_card:
                investor_name = investor_card.find('h2').text.strip()
                investor_type = investor_card.find('a', class_='is-underlined').text.strip()
                locations = [a.text.strip() for a in investor_card.find_all('a', href=lambda href: href and '/investors/by-location/' in href)]
                markets = [a.text.strip().lower() for a in investor_card.find_all('a', href=lambda href: href and '/investors/by-market/' in href)]
                past_investments = [span.text.strip() for span in investor_card.find_all('span', class_='mx-auto has-text-centered')]
                
                # Store investor data
                investors_data.append({
                    "name": investor_name,
                    "type": investor_type,
                    "locations": locations,
                    "markets": markets,
                    "past_investments": past_investments,
                    "url": full_url
                })

# Find the top 3 matching investors
def find_top_investors(user_market, investors_data, k=3):
    matching_investors = []
    
    for investor in investors_data:
        match_count = investor["markets"].count(user_market)
        if match_count > 0:
            matching_investors.append((match_count, investor))
    
    # Sort by the number of matches and get the top k
    matching_investors.sort(reverse=True, key=lambda x: x[0])
    return [investor for _, investor in matching_investors[:k]]

# Get the top 3 investors
top_investors = find_top_investors(user_market, investors_data, k=3)

# Output the results
if top_investors:
    for i, investor in enumerate(top_investors, start=1):
        print(f"\nTop {i} Investor:")
        print("Name:", investor["name"])
        print("Type:", investor["type"])
        print("Locations:", ', '.join(investor["locations"]))
        print("Markets:", ', '.join(investor["markets"]))
        print("Past Investments:", ', '.join(investor["past_investments"]))
        print("Profile URL:", investor["url"])
else:
    print(f"No investors found for the market: {user_market}")
