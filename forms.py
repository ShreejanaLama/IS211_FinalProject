# forms.py

# Importing FlaskForm to create secure HTML forms
from flask_wtf import FlaskForm

# Importing field types
from wtforms import StringField, PasswordField, SubmitField

# Importing validator to make sure fields are not empty
from wtforms.validators import DataRequired

# Creating a login form class using FlaskForm
class LoginForm(FlaskForm):
    # Text input for the username (required)
    username = StringField('Username', validators=[DataRequired()])
    
    # Password input (hidden text, also required)
    password = PasswordField('Password', validators=[DataRequired()])
    
    # Submit button to send the form
    submit = SubmitField('Login')
