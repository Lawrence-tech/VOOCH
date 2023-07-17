from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Add the CORS middleware after creating the Flask app instance
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
# Endpoint for user/reviwer login
login.login_view = 'login'

from app import routes, models
