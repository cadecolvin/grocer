from flask import Flask
from flask import render_template
from flask.ext.bcrypt import Bcrypt

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
