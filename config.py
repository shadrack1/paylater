import os

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'youcanneverguess'
    TESTING = os.environ.get('TESTING')
    FLASK_DEBUG = os.environ.get("FLASK_DEBUG")

