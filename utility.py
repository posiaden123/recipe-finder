import re
from bs4 import BeautifulSoup

def print_ingredients(ing):
    for i in ing:
        print(i.get_text().strip())

def get_ingredients(web: str, soup: BeautifulSoup):
    if web == 'all':
        return soup.find_all('span', {'class': re.compile('ingredients')})
