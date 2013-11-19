#!/usr/bin/env python

from app import app

@app.route('/') # these decorators route a URL to this function
@app.route('/index')
def index():
    return 'Hello World'