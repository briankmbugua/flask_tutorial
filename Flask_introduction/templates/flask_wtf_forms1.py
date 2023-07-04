# Flask-WTF
"""
The Flask-WTF extension makes working with web forms a much more pleasant experience.This extension is a Flask intergration wrapper around the framework-agnostic WTFForm package
"""
# pip install flask-wtf
# Cross-Site Request Forgery(CSRF) Protection
"""By default Flask-WTF proctects all forms against Cross-Site Request Forgery attacks.A CSRF attack occurs when a malicious website sends request to a different website on which the victim is logged in
To implement CSRF protection, Flask-WTF needs the application to configure an encryption key. Flask-WTF uses this key to generate encrypted tokens that are used to verify the authenticity of requests with form data."""

# How to configure an encryption key
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

"""The app.config dictionary is a general-purpose place to store configuration variables used by the framework, the extensions or the application itself.Configuration variables can be added to the app.config dictionary using the standard dictionary syntax, The configuration object also has methods to import configuration values from files or the enviroment"""

# Form Classes
"""When using Flask-WTF, each web form is represented by a class that inherits from class Form.The class defines the list of fields in the form, each represented by an object.Each field can have one or more validators attached."""


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


"""The fields in the form are defined as class variables, and each class variable is assinged an object associated with the field type.
The NameForm form has a text field called name and a submit button called submit.The StringField class represents an <input> element with a type="text" attribute.The SubmitField class represents an <input> element with a type = "submit" attribute.The first argument to field constructors is the label that will be used when rendering the form to HTML
validators argument included in the StringField constructor defines a list of checkers that will be applied to the dat submitted by the user before it is accepted.Required() validator ensures that the field is not submitted empty. """

# HTML Rendering of Forms
"""Form fields are callables that, when invoked from a template render themselves to HTML."""
