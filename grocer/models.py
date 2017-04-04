from . import db
from . import bcrypt
from sqlalchemy.ext.hybrid import hybrid_property

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), unique=True)
    _password = db.Column(db.String(128))
    recipes = db.relationship('Recipe', backref='user')

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plain_text):
        self._password = bcrypt.generate_password_hash(plaintext)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def password_is_correct(self, password):
        return bcrypt.check_password(self._password, password)


class Recipe(db.Model):
    recipe_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    name = db.Column(db.String(64))
    description = db.Column(db.String(128))

    steps = db.relationship('RecipeStep', backref='recipe')
    ingredients = db.relationship('RecipeIngredient', backref='recipe')

    def __init__(self, user_id, name, description):
        self.user_id = user_id
        self.name = name
        self.description = description


class RecipeStep(db.Model):
    recipestep_id = db.Column(db.Integer, primary_key=True,
            autoincrement=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'))
    ordinal = db.Column(db.Integer)
    name = db.Column(db.String(64))
    step_text = db.Column(db.Text)

    def __init__(self, ordinal, name, text):
        self.ordinal = ordinal
        self.name = name
        self.text = text


class RecipeIngredient(db.Model):
    recipeingredient_id = db.Column(db.Integer, primary_key=True,
            autoincrement=True)
    recipe_id = db.Column(db.Integer,
            db.ForeignKey('recipe.recipe_id'))
    ingredient_id = db.Column(db.Integer,
            db.ForeignKey('ingredient.ingredient_id'))
    measurement_id = db.Column(db.Integer,
            db.ForeignKey('measurement.measurement_id'))
    amount = db.Column(db.Float)

    #TODO: Determine how to properly handle this relationship
    
    ingredient = db.relationship('Ingredient', backref='recipeingredient')
    measurement = db.relationshipt('Measurement', backref='measurement')


class Ingredient(db.Model):
    ingredient_id = db.Column(db.Integer, primary_key=True,
            autoincrement=True)
    name = db.Column(db.String(64))
    calories_per_kg = db.Column(db.Float)

    def __init__(self, name, calories_per_kg):
        self.name = name
        self.calories_per_kg = calories_per_kg


class Measurement(db.Model):
    measurement_id = db.Column(db.Integer, primary_key=True,
            autoincrement=True)
    name = db.Column(db.String(64))
    abbreviation = db.Column(db.String(6))

    def __init__(self, name, abbreviation):
        self.name = name
        self.abbreviation = abbreviation
