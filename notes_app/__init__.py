
from flask import Flask, render_template, request, redirect, url_for, flash # importing Flask obj from "flask" module
# also importing 'render_template' to render HTML templates
# also importing 'request' to house/handle data going from client to server
# also importing 'redirect' and 'url_for' to redirect to other routes
# also importing 'flash' to display user feedback msgs

from flask_sqlalchemy import SQLAlchemy # importing SQLAlchemy obj to interface with our SQLite database

import os # Python's module for interacting with the OS
from dotenv import load_dotenv # this func finds a .env file in the project dir; if it finds one, 
# it loads the environment variables in the file and helps project access them
load_dotenv() # loading our env variables 

notes_app = Flask(__name__) # initializing our app obj with the current module name
notes_app.config["SECRET_KEY"] = os.getenv("SECRET_KEY") # configuring our secret key for Flask web forms here
notes_app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI") # configuring our SQLAlchemy database location (the /// = relative path, so the database will be somewhere in our project directory)
notesDB = SQLAlchemy(notes_app) # initializing our SQLAlchemy obj for use with our app obj

from .forms import AddNote, SignIn, SignUp # importing our Flask form classes
from .models import Note # importing our Flask data models (data model: class that represents a table in the DB)

''' ROUTES ARE BELOW FOR NOW '''

# index route
@notes_app.route('/')
@notes_app.route('/index')
def index():
    return render_template('index.html')







