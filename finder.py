import requests
import sys
import utility
import re
from bs4 import BeautifulSoup

url = input("Paste the url of the page that contains the recipe:")
try:
    page = requests.get(url)
except requests.exceptions.RequestException as e:
    print("Whoops! The page you were trying to reach encountered an error.\nPlease try again later, or run the program again to input a new page.")
    print("Status Code:", e)
    sys.exit()

soup = BeautifulSoup(page.content, 'html.parser')
if 'allrecipes' in str(page.url):
    ingredients = utility.get_ingredients('all', soup)
    directions =
elif 'foodnetwork' in str(page.url):
    a = 0
else:
    ingredients = soup.find_all('div', {'class': re.compile('ingredients')})
    directions = soup.find_all('div', {'class': re.compile("instruction")})


print("There you go! I hope you enjoyed my scraper!")




