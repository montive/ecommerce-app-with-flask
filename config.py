from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    class BaseConfig:
        """Base config."""
        SECRET_KEY = environ.get('SECRET_KEY')
        STATIC_FOLDER = 'static'
        TEMPLATES_FOLDER = 'templates'

    class ProdConfig(BaseConfig):
        FLASK_ENV = 'production'
        DEBUG = False
        TESTING = False
        SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_PROD_DATABASE_URI')

    class DevConfig(BaseConfig):
        FLASK_ENV = 'development'
        DEBUG = True
        TESTING = True
        SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DEV_DATABASE_URI')