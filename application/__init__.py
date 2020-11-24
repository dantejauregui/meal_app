from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.secret_key = 'dev'

# enter path to the sqlite file here. A new db is created if one does not exist.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mealappdb.sqllite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


import application.apiLayer.imageAPI
import application.dataAccessLayer.models

