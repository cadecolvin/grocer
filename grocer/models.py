from . import db
from . import bcrypt
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property


class User(UserMixin, db.Model):
    __tablename__ = 'Users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_id = db.Column(db.Integer, db.ForeignKey('UserRoles.role_id'))
    email = db.Column(db.String(128), unique=True, index=True)
    _password = db.Column(db.String(128))
    identity_confirmed = db.Column(db.Boolean, default=False)

    recipes = db.relationship('Recipe', backref='user') 

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def verify_password(self, password):
        return bcrypt.check_password_hash(self._password, password)


class UserRole(db.Model):
    __tablename__ = 'UserRoles'
    role_id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    default = db.Column(db.Boolean, default=False)

    users = db.relationship('User', backref='role')

    def __init__(self, name, description):
        self.name = name
        self.description = description


class Recipe(db.Model):
    __tablename__ = 'Recipes'
    recipe_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'))
    name = db.Column(db.String(64))
    description = db.Column(db.String(128))

    steps = db.relationship('RecipeStep', backref='recipe')
    ingredients = db.relationship('RecipeIngredient', backref='recipe')

    def __init__(self, user_id, name, description):
        self.user_id = user_id
        self.name = name
        self.description = description


class RecipeStep(db.Model):
    __tablename__ = 'RecipeSteps'
    recipestep_id = db.Column(db.Integer, primary_key=True,
            autoincrement=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('Recipes.recipe_id'))
    ordinal = db.Column(db.Integer)
    name = db.Column(db.String(64))
    step_text = db.Column(db.Text)

    def __init__(self, ordinal, name, text):
        self.ordinal = ordinal
        self.name = name
        self.text = text


class RecipeIngredient(db.Model):
    __tablename__ = 'RecipeIngredients'
    recipeingredient_id = db.Column(db.Integer, primary_key=True,
            autoincrement=True)
    recipe_id = db.Column(db.Integer,
            db.ForeignKey('Recipes.recipe_id'))
    ingredient_id = db.Column(db.Integer,
            db.ForeignKey('Ingredients.ingredient_id'))
    measurement_id = db.Column(db.Integer,
            db.ForeignKey('Measurements.measurement_id'))
    amount = db.Column(db.Float)

    #TODO: Determine how to properly handle this relationship
    
    ingredient = db.relationship('Ingredient', backref='recipeingredient')
    measurement = db.relationship('Measurement', backref='measurement')


class Ingredient(db.Model):
    __tablename__ = 'Ingredients'
    ingredient_id = db.Column(db.Integer, primary_key=True,
            autoincrement=True)
    name = db.Column(db.String(64))
    calories_per_kg = db.Column(db.Float)

    def __init__(self, name, calories_per_kg):
        self.name = name
        self.calories_per_kg = calories_per_kg


class Measurement(db.Model):
    __tablename__ = 'Measurements'
    measurement_id = db.Column(db.Integer, primary_key=True,
            autoincrement=True)
    name = db.Column(db.String(64))
    abbreviation = db.Column(db.String(6))

    def __init__(self, name, abbreviation):
        self.name = name
        self.abbreviation = abbreviation


class Meal(db.Model):
    __tablename__ = 'Meals'
    meal_id = db.Column(db.Integer, primary_key=True,
            autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('Recipes.recipe_id'))
    meal_dt = db.Column(db.Date)

    user = db.relationship('User', backref='user')
    recipe = db.relationship('Recipe', backref='meal')

    def __init__(self, user, recipe, meal_date):
        self.user_id = user.user_id
        self.recipe_id = recipe.recipe_id
        self.meal_dt = meal_date
