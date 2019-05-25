"""
@ Author  Atul
"""
from pathlib import Path


class BaseConfig:
    SECRET_KEY = r'f\x13\xd9fM\xdc\x82\x01b\xdb\x03'


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///{0}/test.db".format(Path(__file__).parent)


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True


class ProdConfig(DevConfig):
    DEBUG = False




api_config = {
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig
}
