# Student management system
A small student management system to demonstrate how to use the Flask-SQLAlchemy extension
# 1.Install Flask and Flask-SQLAlchemy
# 2.Setting up the Database and Model
In this step, i'll set up the database connection, and create an SQLAlchemy database model, which is a python class that represents the table that stores your data.I'll initiate the database, create a table for students based on the model declared, and add a few students into the students table
# Setting up the database connection
the database URI and other configurations which are put in app.config
# Creating the database
set the app.py file as your Flask application using the FLASK_APP enviromental variable.
Import the database and the Model in this case student, then use db.create_all() method to create the table in the database
# NOTE:
The db.create_all() function does not recreate or update a table if it already exists in the database.To modify the model you have to delete all existing database tables with db.drop_all() function and then recreate the with db.create all().This will apply the modifications you make to your models, but will also delete all the existing data in the database.To update the database and preserve existing data you'll need to use schema migration which allows you to modify your tables and preserve data.
```bash
export FLASK_APP=app
flask shell
>>> from app import db, Student
>>> db.create_all()
```