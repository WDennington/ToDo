from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config["SECRET_KEY"] = SECRET_KEY

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

from application import routes