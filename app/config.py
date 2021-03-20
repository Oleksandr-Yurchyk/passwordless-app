from datetime import timedelta

from decouple import config

# General
DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY')

# DB
HOST = config('PUBLIC_HOST')
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False

# Flask session
PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)
TOKEN_TIME_EXPIRED_IN_MIN = 3

# Gmail server
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = config('MAIL_USERNAME')
MAIL_PASSWORD = config('MAIL_PASSWORD')

# administrator list
ADMIN = [config('MAIN_ADMIN')]
