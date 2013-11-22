#!/usr/bin/env python

from flask import Flask
from flask.ext.sqlachemy import SQLAchemy

app = Flask(__name__) # create the application object
app.config.from_object('config')
db = SQLAchemy(app)

# views are handlers that manage requests
from app import views, models