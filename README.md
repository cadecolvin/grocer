# Grocer #

## Description ##
Grocer is your personal grocery list assistant. It will automatically build a meal plan and grocery list for you based on your recipe library.

You can use Grocer's default recipe library as a template to add your own custom recipes.

## Use ##
You can add custom recipes by creating a json file in the *recipe-library* folder. The name of the file should be the title of the recipe. The file should be formatted as follows:
'''json
{
    "URL":"URL to the recipe if it exists",
    "Ingredients":[
        ["Quantity", "Quantifier", "Ingredient"],
    ]
    "Instructions":[
        ["Step Number", "Step Title", "Step Text"],
    ]
}
'''

For example, a simple recipe for a bowl of Cap'n Crunch is below
'''json
{
    "URL":"http://www.capncrunch.com/",
    "Ingredients:[
        [".75", "Cup", "Cap'n Crunch"],
        [".75", "Cup", "Milk"]
    ]
    "Instructions":[
        ["1", "Pour Cereal", "Measure out the Cap'n Crunch and pour it into your cereal bowl."],
        ["2", "Pour Milk", "Measure out the milk and pour it over the cereal."],
        ["3", "Enjoy!", "Eat the cereal as quickly as possible to ensure that the roof of your mouth is completely destroyed."]
    ]
}

## Development ##
Currently no third party libraries are required for the main project. Within the *Utilities* directory, you will find a Pip *requirements* file as the recipe scrapers require a few 3rd party libraries in order to run.
