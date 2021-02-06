import requests
import sys
import utility
import re
from bs4 import BeautifulSoup

print("Due to the way some pages set up their website, some directions might get printed multiple times!")
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
    directions = utility.get_directions('all', soup)
    print("Ingredients:\n")
    utility.print_ingredients(ingredients)
    utility.print_allrec_directions(directions)
    print('\n\nThere you go! I hope you enjoyed my recipe finder!')
    sys.exit()
if 'foodnetwork' in str(page.url):
    ingredients = utility.get_ingredients('food', soup)
    directions = utility.get_directions('food', soup)
    utility.print_food_ingredients(ingredients)
    print('\n')
    utility.print_food_directions(directions)
    print('\n\nThere you go! I hope you enjoyed my recipe finder!')
    sys.exit()

ingredients = soup.find_all('div', {'class': re.compile('ingredients')})
directions = soup.find_all('div', {'class': re.compile("instruction")})
utility.print_ingredients(ingredients)
utility.print_directions(directions)
print('\n\nThere you go! I hope you enjoyed my recipe finder!')




