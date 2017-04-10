from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from . import recipes
from .. import db
from ..models import Recipe, RecipeStep, Ingredient, Measurement

@recipes.route('/')
@login_required
def recipes():
    return render_template('recipes/index.html')
