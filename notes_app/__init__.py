
from flask import Flask # importing Flask obj from "flask" module

notes_app = Flask(__name__) # initializing our app obj with the current module name

@notes_app.route('/')
@notes_app.route('/index')
def index():
    return "This is a homepage!"