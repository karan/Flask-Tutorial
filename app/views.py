#!/usr/bin/env python

from flask import render_template
from app import app

@app.route('/') # these decorators route a URL to this function
@app.route('/index')
def index():
    user = {'nickname': 'Karan'} # fake user
    return render_template('index.html', title='Home', user=user)