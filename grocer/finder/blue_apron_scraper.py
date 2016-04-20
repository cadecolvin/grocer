import requests
from bs4 import BeautifulSoup
from grocer.core.ingredient import *

ingredients = list()

recipe_url = "https://www.blueapron.com/recipes/gnocchi-caprese-with-garlic-toasts-butter-lettuce-salad"

response = requests.get(recipe_url)
raw_soup = BeautifulSoup(response.text)

ingredients_element = raw_soup.find_all("li", attrs={"itemprop" : "ingredients"})

for ingredient_element in ingredients_element:
    print(ingredient_element.contents[1].contents[1].text)
    print(ingredient_element.contents[1].contents[2])


