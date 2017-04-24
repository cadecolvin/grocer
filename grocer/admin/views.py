from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from . import admin
from ..import db
from ..models import User, Ingredient, Measurement


@admin.route('/ingredients', methods=['GET', 'POST'])
def ingredients():
    ingredient_list = Ingredient.query.all()
    return render_template('admin/ingredients.html',
            ingredients=ingredient_list)
