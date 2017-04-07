from flask import render_template
from flask import session
from flask import redirect
from flask import url_for
from flask import current_app
from .. import db
from . import core


@core.route('/')
def index():
    return render_template('index.html')
