
from os import environ , path



class Config:

    TESTING = environ.get('TESTING')
    FLASK_DEBUG = environ.get('FLASK_DEBUG')
    SECRET_KEY = 'TicketBookingSystem'

    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///MovieTicketDatabase'#environ.get('SQLALCHEMY_DATABASE_URI') # #
    SQLALCHEMY_TRACK_MODIFICATIONS = False #environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')





key = Config.SECRET_KEY