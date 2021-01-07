from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object( os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONANS'] = False
db = SQLAlchemy(app)

from entities.user import User
from entities.article import Article

@app.route('/')
def hello():
    return "Hello World"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()