#!/usr/bin/env python

from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Flash: Form submit with openid = %s and remember me = %s' %
              (str(form.openid.data), str(form.remember_me.data)))
        return redirect('/login')
    return render_template('login.html', title="Sign In",
                           form=form, providers=app.config['OPENID_PROVIDERS'])