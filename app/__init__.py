# Inicjalizacja aplikacji

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'SekretnyKlucz'
db = SQLAlchemy(app)

from app import routes