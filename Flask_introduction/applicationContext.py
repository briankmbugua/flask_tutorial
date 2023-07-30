from flask import Flask, current_app
app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome!'


# print(current_app.config)
# if you try to access the current_app.config object outside of a view function, you should see the following error
""" python3 applicationContext.py
Traceback (most recent call last):
  File "/home/letbmk/Documents/flask_tutorial/applicationContext.py", line 9, in <module>
    print(current_app.config)
  File "/home/letbmk/Documents/flask_tutorial/venv/lib/python3.10/site-packages/werkzeug/local.py", line 311, in __get__
    obj = instance._get_current_object()
  File "/home/letbmk/Documents/flask_tutorial/venv/lib/python3.10/site-packages/werkzeug/local.py", line 508, in _get_current_object
    raise RuntimeError(unbound_message) from None
RuntimeError: Working outside of application context.

This typically means that you attempted to use functionality that needed
the current application. To solve this, set up an application context
with app.app_context(). See the documentation for more information."""

"""To access objects exposed by the Application and Request contexts outside of a view function, you need to create the appropriate context first"""
# Without a context manager
app_context = app.app_context()
app_context.push()
# print(current_app.config['ENV'])
print(f"debug mode {current_app.config['DEBUG']}")
# print(current_app.config['SECRET_KEY'])
# print(current_app.config['SQLALCHEMY_DATABASE_URI'])
app_context.pop()

# With a context manager
with app.app_context():
    print(f"debug mode {current_app.config['DEBUG']}")


if __name__ == '__main__':
    app.run(debug=True)


# Flask Application Context
"""An active application context is required to make queries and to access db.engine and db.session.This is because the session is scoped to the context so that it is cleaned up properly after every request or CLI command"""
# Automatic Context
"""When flask is handling a request of a CLI command, an application context will automatically be pushed.There there is no need to do anythin special to use the database during requests or CLI commands"""
# Manual context
"""If you try to use the database when an application context is not active, you will see  
'RuntimeError: Working outside of application context'
If you need the database and you don't have the context, you can push one with app_context.This is common when calling db.create_all to create the tables"""
"""
def create_app():
    app = Flask(__name__)
    app.config.from_object("project.config")
    import project.models

    with app.app_context():
        db.create_all()
    return app
"""
