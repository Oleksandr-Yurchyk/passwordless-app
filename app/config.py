from datetime import timedelta

# General
DEBUG = True
SECRET_KEY = 'd1a4771d2f3bd4f561f68f3ad19dc004855fba3db'

# DB
LOCAL_HOST = 'http://127.0.0.1:8000'
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/flask_db'
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
MAIL_USERNAME = 'dmytro.gordon.test'
MAIL_PASSWORD = 'some_test_pass'

# administrator list
ADMIN = ['dmytro.gordon.test@gmail.com']
