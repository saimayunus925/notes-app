
''' all CRUD-related routes go here '''

from flask import Blueprint, render_template, request, redirect, url_for, flash 
# importing Blueprint obj from "flask" module to group all CRUD-related routes together
# also importing 'render_template' to render HTML templates
# also importing 'request' to house/handle data going from client to server
# also importing 'redirect' and 'url_for' to redirect to other routes
# also importing 'flash' to display user feedback msgs

CRUD = Blueprint('CRUD', __name__) # our CRUD blueprint of routes

from .forms import AddNote, DeleteNote, EditNote, SignIn, SignUp # importing our Flask form classes
from .models import Note # importing our Flask data models (data model: class that represents a table in the DB

from notes_app import notesDB # importing our DB object

# 'add note' route -> 'C' part of 'CRUD'
@CRUD.route('/add_note', methods=['POST', 'GET'])
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

# 'edit note' route -> 'U' part of 'CRUD'
@CRUD.route('/edit_note/<int:id>', methods=['POST', 'GET'])
def edit_note(id):
    # the ID of the note we wanna edit is passed in, so we'll use that to get the note
    new_form = EditNote(request.form) # 'edit note' form will probs have same format as 'add note' form
    tbe = Note.query.get_or_404(id) # we query the DB for the note we need; if we can't find it, we return a 404 error; else, we get the correct note. also, 'tbe/TBE' = 'to be edited' here
    # TBE note contents will be used as placeholders for new form
    if request.method == "POST" and new_form.validate():
        # if data is POSTed and valid, insert new note data into DB
        tbe.title = new_form.title.data
        tbe.content = new_form.content.data
        notesDB.session.commit() # commit the change
        flash(f"Note '{tbe.title}' edited successfully!") # success feedback msg
        return redirect(url_for("index")) # redirect back to home page
    else:
        # no data POSTed? 
        return render_template('edit_note.html', tbe=tbe, new_form=new_form) # return 'edit note' pg with current note TBE and with 'edit note' form

# 'delete note' route -> 'D' part of 'CRUD'
@CRUD.route('/delete_note/<int:id>', methods=['POST', 'GET'])
def delete_note(id):
    # 1) using passed-in ID, query DB for note to be deleted (TBD/tbd)
    tbd = Note.query.get_or_404(id)
    title = tbd.title
    # 2) initialize 'DeleteNote' form
    form = DeleteNote(request.form)
    if request.method == 'POST' and form.validate():
        # if data (note title) is POSTing and is valid, delete 'tbd' note from DB
        notesDB.session.delete(tbd)
        notesDB.session.commit() # commit the change
        flash(f"Note '{title}' deleted successfully!") # success feedback msg
        return redirect(url_for("index")) # redirect back to home page
    else:
        return render_template('delete_note.html', tbd=tbd, form=form)
