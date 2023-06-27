from flask import Flask, current_app
app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome!'



#print(current_app.config)

#if you try to access the current_app.config object outside of a view function, you should see the following error
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
#Without a context manager
# app_context = app.app_context()
# app_context.push()
# #print(current_app.config['ENV'])
# print(f"debug mode {current_app.config['DEBUG']}")
# #print(current_app.config['SECRET_KEY'])
# #print(current_app.config['SQLALCHEMY_DATABASE_URI'])
# app_context.pop()

# With a context manager
with app.app_context():
     print(f"debug mode {current_app.config['DEBUG']}")






if __name__ == '__main__':
    app.run(debug=True)