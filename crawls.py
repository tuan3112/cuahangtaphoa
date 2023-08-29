
import requests
from bs4 import BeautifulSoup 
from openpyxl import Workbook 

# Send a Get request to the URL

url = "https://www.google.com/search?q=du+h%E1%BB%8Dc+uk&oq=du+h%E1%BB%8Dc+uk&aqs=chrome..69i57.13228j0j1&sourceid=chrome&ie=UTF-8"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all search result elements
search_results = soup.find_all("div", class_="yuRUbf")

# Extract and print the website URLs
for result in search_results:
    # Get the first link in each search result
    link = result.find("a")
    if link:
        # Extract the href attribute, which contains the URL
        url = link.get("href")
        print(url)