import os

class DevConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    