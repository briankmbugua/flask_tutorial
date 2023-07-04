# BASIC APP STRUCTURE
# intialization
"""All flask applications must create an application instance.The web server passes all requests it receives from clients to this object for handling, using a protocal called Server Gateway Interface.The application instance is an object called Flask, created as follows"""

from flask import Flask

app = Flask(__name__)
"""The only required argument to the Flask class constructor is the name of the main module or package of the application.For most applications, python's __name__ variable is the correct value.Flask uses this __name__ argument to determine the root path of the application so that it later can find the resources file relative to the location of the application"""

#Routes and View Functions
"""The application instance needs to know what code need to run for each URL requested, so it keeps a mapping of URLs to Python functions.The association between a URL and the function that handles it is called a route.The most convinient wat to define a route in a Flask application is through the app.route decorator exposed by the application instance.Which registers the decorated function as a route."""

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

"""Functions like index() are called view functions.A response returned by a view function can be a simple string with HTML content, or more complex forms"""
"""The following example defines a route that has a dynamic name component"""

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!<h1>' % name

"""The portion enclosed in angle brackets is the dynamic part, so any URLs that match the static portions will be mapped to this route.When the view function is invoked, Flask sends the dynamic component as an argument.The dynamic components in routes are string by default but can also be defined with a type e.g /user/<int:id> would match only URLs that have an integer in the id dynamic segment.Flask supports types int, float, and path for routes.The path type also represents a string but does not consider slashes as separators and insted considers them part of the dynamic component"""

# SERVER STARTUP
"""The application instance has a run method that launches Flask's intergrated development server."""

if __name__ == '__main__':
    app.run(debug=True)
