import requests
from bs4 import BeautifulSoup
from grocer.core import Ingredient


def get_ingredients(recipe_url):
    ingredients = list()
    response = requests.get(recipe_url)
    raw_soup = BeautifulSoup(response.text, "lxml")

    ingredients_element = raw_soup.find_all("li", attrs={'itemprop': 'ingredients'})

    for ingredient_element in ingredients_element:
        amount = ingredient_element.contents[1].contents[1].text
        name = ingredient_element.contents[1].contents[2]
        ingredients.append(Ingredient(name, amount))

    return ingredients


if __name__ == '__main__':
    url = 'https://www.blueapron.com/recipes/gnocchi-caprese-with-garlic-toasts-butter-lettuce-salad'
    print(get_ingredients(url))
