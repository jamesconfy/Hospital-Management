import os

from flask_sqlalchemy import SQLAlchemy

class DevConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = "sqlite:///sites.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    