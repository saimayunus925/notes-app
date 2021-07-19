
from flask import Flask # importing Flask obj from "flask" module
from flask_pymongo import PyMongo # importing PyMongo() obj to connect/interface with our MongoDB database
from .forms import AddNote # testing if we can import from 'forms.py' 

import os # Python's module for interacting with the OS
from dotenv import load_dotenv # this func finds a .env file in the project dir; if it finds one, 
# it loads the environment variables in the file and helps project access them
load_dotenv() # loading our env variables 

notes_app = Flask(__name__) # initializing our app obj with the current module name
notes_app.config["MONGO_URI"] = os.getenv("MONGO_URI") # configuring the DB's location here
notesDB = PyMongo(notes_app) # initializing PyMongo() obj for use with our app obj

''' ROUTES ARE BELOW FOR NOW '''

# index route
@notes_app.route('/')
@notes_app.route('/index')
def index():
    return "This is a homepage!"

# 'add note' route
@notes_app.route('/add_note')
def add_note():
    pass





