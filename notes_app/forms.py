
# import Form obj (our forms inherit from it), form field objs, and form validators from wtforms library
from wtforms import Form, StringField, PasswordField, SubmitField, TextAreaField, validators

# 'add note' form
class AddNote(Form):
    title = StringField('Title', [validators.DataRequired()]) # note title, can't be empty
    content = TextAreaField('Content', [validators.DataRequired()]) # note content, also can't be empty
    submit_button = SubmitField('Add Note') # the 'submit' button for the 'add-note' form

# 'register' form
class SignUp(Form):
    username = StringField('Username', [validators.DataRequired()]) # account username, can't be empty
    email = StringField('Email', [validators.DataRequired(), validators.Email()]) # account email, can't be empty and must be an email address
    password = PasswordField('Password', [
        validators.Length(min=12, message="ERROR - password must be at least 12 characters long."),
        validators.DataRequired('confirm_password', message="ERROR - new password and confirmed password don't match")
    ]) # account password, can't be empty and must be at least 12 chars long, also must match 'confirm password' field
    confirm_password = PasswordField('Confirm Password', [validators.DataRequired()]) # this field helps us confirm our password by typing it again, can't be empty ofc
    submit_button = SubmitField('Sign Up') # the 'submit' button for the signup form

# 'login' form
class SignIn(Form):
    username = StringField('Username', [validators.DataRequired()]) # account username, can't be empty
    password = PasswordField('Password', [validators.Length(min=12), validators.DataRequired()]) # account password, can't be empty and must be at least 12 chars long
    submit_button = SubmitField('Sign In') # the 'submit' button for the sign-in form