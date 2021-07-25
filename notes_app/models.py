
# our app's Flask-SQlAlchemy data models all go here
# Python data models -> classes that represent our DB's tables

from notes_app import notesDB # importing our SQLAlchemy DB obj with which to interface with our SQLite database
from datetime import datetime # use this to get date/time objs

# 'User' class/model/table
class User(notesDB.Model):
    id = notesDB.Column(notesDB.Integer, primary_key=True) # unique ID/primary key for each 'user' record in the 'users' table
    username = notesDB.Column(notesDB.String(180), unique=True, nullable=False) # user username, 180 chars max, MUST be unique, CANNOT be empty
    email = notesDB.Column(notesDB.String(220), unique=True, nullable=False) # user email, 220 chars max, MUST be unique, CANNOT be empty

    def __repr__(self):
        # this is how User objs will be printed
        return f"<User: {self.username}, {self.email}>"

# 'Note' class/model/table
class Note(notesDB.Model):
    id = notesDB.Column(notesDB.Integer, primary_key=True) # unique ID/primary key for each 'note' record in the 'notes' table
    title = notesDB.Column(notesDB.String(150), nullable=False) # note title, 150 chars max, CANNOT be empty
    date_created = notesDB.Column(notesDB.DateTime, default=datetime.utcnow()) # automatically set to the date a note was created, default is current date/time
    content = notesDB.Column(notesDB.Text, nullable=False) # note content, no max length, CANNOT be empty

    def __repr__(self):
        # this is how Note objs will be printed
        return f"<Note: {self.title}, {self.date_created}, {self.content}>"

notesDB.create_all() # now that our data models have been created (we just have our 'Note' model for now), let's create the DB