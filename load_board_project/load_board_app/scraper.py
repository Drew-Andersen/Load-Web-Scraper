import requests
from bs4 import BeautifulSoup

def scrape_load_board():
    url = "https://example.com" # Replace the example with the real URL
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    load_listings = []

    for load in soup.find_all('div', class_='load-card'):
        load_title = load.find('h2', class_='load-title').text.strip()
        pickup_location = load.find('span', class_='pickup-location').text.strip()
        dropoff_location = load.find('span', class_='dropoff-location').text.strip()
        pay_rate = load.find('span', class_='pay-rate').text.strip()
        load_details_link = load.find('a', class_='load-details-link')['href']

        load_listings.append({
            'title': load_title,
            'pickup_location': pickup_location,
            'dropoff_location': dropoff_location,
            'pay_rate': pay_rate,
            'link': load_details_link
        })

    return load_listings