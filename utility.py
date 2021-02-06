import re
from bs4 import BeautifulSoup

def print_ingredients(ing):
    for i in ing:
        print(i.get_text().strip())

def print_directions(dir):
    for i in dir:
        print(i.text)

def get_ingredients(web: str, soup: BeautifulSoup):
    if web == 'all':
        return soup.find_all('span', {'class': re.compile('ingredients')})
    elif web == 'food':
        return  soup.find_all('span', {'class': re.compile('o-Ingredients__a-Ingredient')})
def print_food_ingredients(ing):
    print("Ingredients:\n")
    for i in ing:
        print(i.get_text().strip())

def print_allrec_directions(dir):
    print("Directions:\n")
    for i in dir:
        print(i.get_text().strip())

def get_directions(web:str, soup: BeautifulSoup):
    if web == 'all':
        return soup.find_all('div', {'class' : 'paragraph'})
    if web == 'food':
        return soup.find_all('li', {'class': 'o-Method__m-Step'})
def print_food_directions(dir):
    print("Directions:\n")
    for i in dir:
        print(i.get_text().strip())



