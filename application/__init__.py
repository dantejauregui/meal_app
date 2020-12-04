import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
#app.secret_key = 'dev'

CORS(app, automatic_options=True)
cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})

# enter path to the sqlite file here. A new db is created if one does not exist.
env_name = os.getenv('environment')
if (env_name == 'production'):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mealappdb.sqllite'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'

db = SQLAlchemy(app)


import application.apiLayer.imageAPI
import application.dataAccessLayer.models

