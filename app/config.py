
from os import environ , path



class Config:

    TESTING = environ.get('TESTING')
    FLASK_DEBUG = environ.get('FLASK_DEBUG')
    SECRET_KEY = 'TicketBookingSystem'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///MovieTicketDatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///Test_MovieTicketDatabase" 
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_type = dict(dev=DevelopmentConfig, test=TestingConfig)

key = Config.SECRET_KEY