
from flask import Flask # importing Flask obj from "flask" module
from flask_pymongo import PyMongo # importing PyMongo() obj to connect/interface with our MongoDB database

notes_app = Flask(__name__) # initializing our app obj with the current module name
notes_app.config["MONGO_URI"] = "" # configuring the DB's location here
notesDB = PyMongo(notes_app) # initializing PyMongo() obj for use with our app obj

''' ROUTES ARE BELOW FOR NOW '''

@notes_app.route('/')
@notes_app.route('/index')
def index():
    n = AddNote()
    return n





