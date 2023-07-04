# FLask redirect and errors
"""The Flask class has a redirect() function.When invoked, it returns a response object and redirects the user to another target location with the specified status code."""

# sysntax
"""Flask.redirect(location, statuscode, response)

- The location parameter is the URL where the response should be redirected
- statuscode is sent to the browser header by default 302
- The response parameter is used to instantiate the response"""

# Initialize the Flask application
from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('log_in.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['usename'] == 'admin':
            return redirect(url_for('success'))
        else:
            abort(401)
    else:
        return redirect(url_for('index'))


@app.route('/success')
def success():
    return 'logged in succesfully'


if __name__ == '__main__':
    app.run(debug=True)
