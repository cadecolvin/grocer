import sys

from bs4 import BeautifulSoup


def pull_recipe_page(recipe_url):
    pass

def parse_ingredients(recipe_html):
    pass

def parse_instructions(recipe_html):
    pass

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
    url = sys.args[1]
    recipe = pull_recipe_page(url)
    ingredients = parse_ingredients(recipe)
    instructions = parse_instructions(recipe)
