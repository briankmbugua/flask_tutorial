"""Flask provides a really simple way to give feedback to a user with the flashing system.The flashing system basically makes it possible to record a message at the end of a request and access it next request and only next request.This is usually combined with a layout template that does this."""

# Simple flashing
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)

app.secret_key = 'hard to guess string'


@app.route('/')
def index():
    return render_template('index4.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


if __name__ == "__main__":
    app.run(debug=True)
