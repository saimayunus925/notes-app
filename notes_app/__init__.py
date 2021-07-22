
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
notes_app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI") # configuring our SQLAlchemy database location 
notesDB = SQLAlchemy(notes_app) # initializing our SQLAlchemy obj for use with our app obj

from .forms import AddNote, SignIn, SignUp # importing our Flask form classes
from .models import Note # importing our Flask data models (data model: class that represents a table in the DB)

''' ROUTES ARE BELOW FOR NOW '''

# index route
@notes_app.route('/')
@notes_app.route('/index')
def index():
    return render_template('index.html')

# 'add note' route -> 'C' part of 'CRUD'
@notes_app.route('/add_note', methods=['POST', 'GET'])
def add_note():
    notes_form = AddNote(request.form) # take 'note form' data values from 'request' obj, assign them to 'notes_form' properties to get our final 'note form' obj
    if request.method == 'POST' and notes_form.validate():
        # if 'note form' data is POSTing and valid, put the data in a new Note() obj and insert obj into DB
        new_note = Note(title=notes_form.title.data, content=notes_form.content.data) # 'Note' object with our 'note form' data -> basically, our new note
        notesDB.session.add(new_note) # insert new note into DB
        notesDB.session.commit() # commit the change
        flash("Note added successfully!") # success feedback msg
        return redirect(url_for("index")) # redirect to home page
    else:
        # no data POSTing? return 'add note' pg
        return render_template('add_note.html', notes_form=notes_form)





