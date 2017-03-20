import json
import requests
import sys
import unicodedata

from bs4 import BeautifulSoup

def parse_title(recipe_url):
    title_idx = recipe_url.find('recipes/')
    title = recipe_url[title_idx:]
    title = title.replace('recipes/', '')
    return title

def pull_recipe_page(recipe_url):
    page = requests.get(recipe_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def parse_ingredients(recipe_soup):
    ingredients = []
    ingr_section = recipe_soup.find('section', attrs={'id':'ingredients'})
    ingr_list = ingr_section.findAll('li', attrs={'itemprop':'ingredients'})

    for item in ingr_list:
        quantity = item.find('span', {'class':'amount'}).text
        full_name = item.text.replace(quantity, '').strip()

        # The quantifier is always the first word of the full name
        quantifier = full_name.split(' ')[0]

        # If the full_name is only the quantifier set the name as
        # the quantifier
        if(full_name != quantifier):
            name = full_name.replace(quantifier, '')
        else:
            name = quantifier

        try:
            quantity = unicodedata.numeric(quantity)
            quantity = '{0:.2f}'.format(quantity)
        except:
            pass

        ingredients.append([quantity, quantifier, name])

    return ingredients

def parse_instructions(recipe_soup):
    instructions = []
    instr_section = recipe_soup.find('section', {'id':'instructions'})
    instr_rows = instr_section.findAll('div', {'class':'step-row row'})
    for row in instr_rows:
        for instr in row.findAll('div', {'class':'instr-wrap'}):
            step_num = instr.find('span', 
                                    {'class':'instr-num'}).text.strip()
            step_title = instr.find('span',
                                    {'class':'instr-title'}).text.strip()
            step_text = instr.find('div',
                                    {'class':'instr-txt'}).text.strip()

            step_text = step_text.replace('\n', ' ')
            instructions.append([step_num, step_title, step_text])

    return instructions

if __name__ == '__main__':
    url = sys.argv[1]
    title = parse_title(url)
    recipe = pull_recipe_page(url)
    ingredients = parse_ingredients(recipe)
    instructions = parse_instructions(recipe)

    with open(f'{title}.json', 'wt') as f:
        json.dump({'URL':url,
                   'Ingredients':ingredients, 
                   'Instructions':instructions}, f)
