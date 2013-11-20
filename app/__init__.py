#!/usr/bin/env python

from flask import Flask

app = Flask(__name__) # create the application object
app.config.from_object('config')

from app import views # views are handlers that manage requests