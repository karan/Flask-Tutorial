#!/usr/bin/env python

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__) # create the application object
app.config.from_object('config')
db = SQLAlchemy(app)

# views are handlers that manage requests
from app import views, models