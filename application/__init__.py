from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'dev'

# enter path to the sqlite file here. A new db is created if one does not exist.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mealappdbsqlite'

db = SQLAlchemy(app)


from application.apiLayer.imageAPI import app
from application.dataAccessLayer import models

