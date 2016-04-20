import requests
from bs4 import BeautifulSoup

from src.core.ingredient import Ingredient

ingredients = list()

recipe_url = "https://www.blueapron.com/recipes/gnocchi-caprese-with-garlic-toasts-butter-lettuce-salad"

response = requests.get(recipe_url)
raw_soup = BeautifulSoup(response.text)

ingredients_element = raw_soup.find_all("li", attrs={"itemprop" : "ingredients"})

for ingredient_element in ingredients_element:
    ingredients.append(new Ingredient(ingredient_element))
