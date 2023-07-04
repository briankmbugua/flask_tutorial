import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
# helper function to help in accessing SQL functions
from sqlalchemy.sql import func

app = Flask(__name__)
# configuring database connection
# the database URI
databaseURI = 'mysql+pymysql://root:password@localhost:3306/student_management_system'
app.config['SQLALCHEMY_DATABASE_URI'] = databaseURI
# disabling tracking of changes in objects in order to save memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Declaring the table
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    create_at = db.Column(db.DateTime(timezone=True),
                          server_default=func.now())
    bio = db.Column(db.Text)

    def __repr__(self):
        return f'<Student {self.firstname}'


# Creating the database
# Use the Flask shell to create your database and your student table based on the Student model.Also set the app.py file as your Flask application using the FLASK_APP enviromental variable.
