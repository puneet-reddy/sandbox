#!/usr/bin/env python

import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_settings():
    app_settings = os.getenv('APP_SETTINGS')

    if app_settings == 'prod':
        app_settings = 'api.config.ProdConofig'
    elif app_settings == 'dev':
        app_settings = 'api.config.DevConfig'
    elif app_settings == 'test':
        app_settings = 'api.config.TestConfig'
    else:
        app_settings = 'api.config.LocalConfig'

app.config.from_object(get_settings())

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from api.views import compare_blueprint
app.register_blueprint(compare_blueprint)