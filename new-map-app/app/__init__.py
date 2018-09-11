
from flask import Flask
import os


app = Flask(__name__)

# app.config.from_pyfile('config.py')
app.config['DEBUG'] = True


from app import views
