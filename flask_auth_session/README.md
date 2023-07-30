# INTRO
A session is nearly identical to a cookie in terms of idea.
Session data is saved on the server.It may be defined as the time taken by the user to log in and out of the server.

# creating a session in flask
- provide the s SECRET_KEY to encrypt the session on the server app.config['SECRET_KEY]
- if it's a permanent session provide PERMANENT_SESSION_LIFETIME in app.config["PERMANENT_SESSION_LIFETIME"]

session in python are represented as dictionaries


# Flask Session
Flask-Session is an extension that support the Sever-side Session management in a flask application
A session is the amount of time spent on a particular activity.A user session begins when a user sings in to or uses a specific computer, network, or a software service in a computer system.The data to be saved in the session is stored in the temporary directory on the server.Each client will have their session, and their data will be held in their respective session.
# Why Session Are Necessary
It lets the server know when the user logs in.
# Installation
```bash
$: pip install flask-session
```
# configuration
- SESSION_PERMANENT = False - Here the session has a default time limit, after which it will expire
- SESSION_TYPE = "file" - it will get stored in a hard drive or any online idle account.It also acts as an alternative to the databas
- SECRET_KEY - Should be set to secure the app


# Flask-Login
It provides user session management in Flask.It controls the everyday tasks of logging in, logginh out, and rembering your users' sessions for a long time

Flask-Login is not restricted to any particular database system or permissions model.The only requirments are that your user objects implement a few methods and that you supply a callback to the extension that can load information from our database object(here it is dictionary object, students)

# Installation
```bash
$: pip install flask-login
```