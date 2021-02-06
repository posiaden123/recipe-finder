import requests
import sys
from bs4 import BeautifulSoup

url = input("Paste the url of the page that contains the recipe:")
try:
    page = requests.get(url)
except requests.exceptions.HTTPError as e:
    print("Whoops! The page you were trying to reach encountered an error. Please try again later, or input a new page")
    print("Status Code", e)
    sys.exit()
soup = BeautifulSoup(page, 'html.parser')



