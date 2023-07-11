import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Define a secret key to enable session
    SECRET_KEY = os.environ.get("APP_SECRET_KEY") or "default_secret_key"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'vooch.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
