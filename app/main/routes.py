from flask import render_template, flash, redirect, url_for, request
from app import db
from app.main import bp
from app.models import *
from app.main.forms import *

@bp.route('/')
@bp.route('/index')
def index():
    #return "Hello World. This is a flask boilerplate with flask-sqlalchemy and flask-migrate"
    return render_template('index.html')