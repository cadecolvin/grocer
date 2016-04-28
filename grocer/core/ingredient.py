class Ingredient:
    name = ""
    amount = 0

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return str.format("{0} {1}", "why", "not")
