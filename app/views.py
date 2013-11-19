#!/usr/bin/env python

from flask import render_template
from app import app

@app.route('/') # these decorators route a URL to this function
@app.route('/index')
def index():
    user = {'nickname': 'Karan'} # fake user
    posts = [
        {'author': {'nickname': 'Bill Clinton'},
         'body': 'Binder full of women!'
        },
        {'author': {'nickname': 'Who?'},
         'body': 'There goes my baby...'
        }
    ]
    return render_template('index.html', title='Home',
                           user=user, posts=posts)