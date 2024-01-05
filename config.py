import os


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL')


class ProductionConfig(Config):
     SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URL')
     DEBUG = False


config_options = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
)

