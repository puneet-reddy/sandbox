#!/usr/bin/env python

'''
All configuration goes here
'''

import os
basedir = os.path.abspath(os.path.dirname(__file__))
sqlitedb = 'sqlite:///' + os.path.join(basedir, 'app.db')


class Config(object):
    '''Configuration base class'''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'somethingsecret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', default=sqlitedb)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', default=25))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', default=None)
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['puneet.reddy@gmail.com']
    POSTS_PER_PAGE = 3
