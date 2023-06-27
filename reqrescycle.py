from flask import Flask

app = Flask(__name__)


"""when flask receives a request from the client, it needs to make a few objects available to the view function that will handle it.A good example is the request object which enscapulates the HTTP request sent by the client.
Flask doesn't send the request object to the view function as an argument as this would claater the view function with arguments considering that the request object is not the only object that the view function would need to fulfil a client's request.
To avoid this flask uses contexts to temporarily make certain objects globally accessible."""

from flask import request

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s<p>' % user_agent

if __name__== '__main__':
    app.run(debug=True, port=8080)

"""In the code above notice how in this view function request is used as if it were a global variable.In reality request cannot be a global variable if you consider that in a multithreaded server the threads are working on different requests from different clients at the same time.so each thread needs to see a different object in request.Contexts enables Flask to make certain variables globally accessible to a thread without interfering with the other threads."""

# Flask context globals
"""
current_app - Application context - the application instance for the active application
b\

g - Application context - An object that the application can use for temporary storage during the handling of a request.This variable is reset with each request.

request - Request context - The request object which encapsulates the contents of a HTTP request sent by the client.

session - Request context - The user session, a dictionary that the application can use to store values that are "remembered" between requests.

Flask activates or pushes the application and request contexts before dispatching a request and then removes them when the request is handled.
"""

