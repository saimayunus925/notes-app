
from notes_app import notes_app # importing our app object

if __name__ == "__main__": 
    # if the current module's name == the main program's name, i.e. if the current module is the main program
    # then the app will run in debug mode (server updates upon code changes)
    notes_app.run(debug=True)