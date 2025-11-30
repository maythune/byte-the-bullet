import requests
from bs4 import BeautifulSoup

# Replace with the URL you want to scrape
TARGET_URL = 'https://www.example.com' 

def scrape_data(url):
    """Fetches the HTML and extracts a specific element."""
    try:
        # Use a User-Agent header to mimic a real browser
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Raise an exception for bad status codes

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # --- Extraction Logic (This is the critical part) ---
        # Find the main <h1> tag on the example website
        target_element = soup.find('h1')

        if target_element:
            return f"The main headline is: {target_element.text.strip()}"
        else:
            return "Could not find the target information on the page."

    except requests.exceptions.RequestException as e:
        return f"Error connecting to the website: {e}"

# Example test run (you can comment this out later)
# if name == "main":
#     print(scrape_data(TARGET_URL))