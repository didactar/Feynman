import os


class Config():
    DEBUG = os.environ['DEBUG']
    DEVELOPMENT = os.environ['DEVELOPMENT']
    TESTING = os.environ['TESTING']
    SQLALCHEMY_DATABASE_URI = os.environ['SQL_URI']
    SECRET_KEY = os.environ['SECRET_KEY']
    SERVER_NAME = os.environ['SERVER_NAME']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
