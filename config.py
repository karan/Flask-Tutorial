#!/usr/bin/env python

import os

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'tis-my-key'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]


# required by flask, path to the database file
SQLACHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# folder to store migrate data files
SQLACHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')