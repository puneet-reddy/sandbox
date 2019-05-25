#!/usr/bin/env python

import os

POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
POSTGRES_PASS = os.getenv('POSTGRES_PASS', 'postgres')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')

postgres_local_base = 'postgresql://{}:{}@{}:{}/'.format(
    POSTGRES_USER, POSTGRES_PASS, POSTGRES_HOST, POSTGRES_PORT)
database_name = os.getenv('HUMANITI_DB', 'humaniti')

class BaseConfig:
    """Base configuration"""
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_development')
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_URL = os.getenv('API_URL', 'http://localhost/')

class LocalConfig(BaseConfig):
    """Local Configuration"""
    DEBUG = True
    SECRET_KEY = 'my_precious_development'

class DevConfig(BaseConfig):
    """Development Configuration"""
    DEBUG = True

class TestConfig(BaseConfig):
    """Testing Configuration"""
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name + '_test'

class ProdConfig(BaseConfig):
    """Production Configuration"""
    DEBUG = False