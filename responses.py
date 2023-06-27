"""When Flask invokes a view function, it expects its return value to be the response to the Request.HTTP response code is part of the response.By default Flask set the 200 succesful request code.When a view function needs to respond with a different status code, it can add the numeric code as a second return value after the response text."""
# @app.route('/')
# def index():
#     return '<h1>Bad Request</h1>', 400   #returning a different status code, responses returned by view functions can also take a third argument, a dictionary of headers that are added to the HTTP response.
"""Instead of returning one, two or three values as a tuple, Flask view functions have the option of returning a Response object.The make_response() function takes one, two or three arguments and returns a Response object.Sometimes it's useful to perform this conversion inside the view function."""

# create a response object and set a cookie in it.

from flask import Flask
from flask import make_response
app = Flask('__main__')

# @app.route('/')
# def index():
#     response = make_response('<h1>This document carries a cookie! </h1>')
#     response.set_cookie('answer', '42')
#     return response

"""There is a special type of response called redirect.This response does not include a page document.It just gives the browser a new URL from which to load a new page.They are typically used with web forms, a redirect is also indicated with a 302 response status code and the URL to redirect to given in a Location header.It can be generated using a three value return, or also with a Response object, but given its frequent use, Flask provides a redirect() helper function that creates this response"""

# from flask import redirect
# @app.route('/')
# def index():
#   return redirect('http://127.0.0.1:8080')

"""Another special response is issued with the abort function, which is used for error handling.Note that abort does not return control back to the function that calls it but gives control back to the web server by raising an exception"""

# from flask import abort
# @app.route('/user/<id>')
# def get_user(id):
#     if id:
#         abort(404)
#     return '<h1>Hello, %s</h1>' % user.name

if __name__ == "__main__":
    app.run(debug=False)

