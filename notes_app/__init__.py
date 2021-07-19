
from flask import Flask, render_template, request, redirect, url_for # importing Flask obj from "flask" module
# also importing 'render_template' to render HTML templates
# also importing 'request' to house/handle data going from client to server
# also importing 'redirect' and 'url_for' to redirect to other routes

from flask_pymongo import PyMongo # importing PyMongo() obj to connect/interface with our MongoDB database
from .forms import AddNote, SignIn, SignUp # testing if we can import from 'forms.py' 

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
    return render_template('index.html')

# 'add note' route
@notes_app.route('/add_note', methods=['POST', 'GET'])
def add_note():
    notes_form = AddNote(request.form) # the KV pairs of form data in our request will go to an AddNote() obj
    # that will be our final 'notes_form' obj
    if request.method == 'POST': 
        # data's been POSTed from 'add note' form? insert that data into our DB
        myNotesTable = notesDB.db # our collection/table of notes
        # new 'note' record/Python dict/JS obj/MongoDB doc, populated by our form data, to insert into our DB
        newNote = {
            "title": notes_form.title.data,
            "content": notes_form.content.data
        }
        myNotesTable.insertOne(newNote) # inserting the 'note' obj/record into our DB
        flash("Note added successfully!") # 'success' feedback msg if note was added correctly
        return redirect(url_for("index")) # return to home page
    else: 
        # no data POSTed? return HTML form page
        return render_template('add_note.html', notes_form=notes_form)





