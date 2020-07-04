#!/usr/bin/env python

from flask_app import app

@app.route('/')
def home():
    return 'Hello world!'