from dotenv import load_dotenv

import os

load_dotenv()

class Development(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class Production(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

configs = {
    'development': Development,
    'production': Production,
}