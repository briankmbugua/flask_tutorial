# FLASK-MOMENT
"""There is an execellent client-side open source library written in javascript that renders dates and times in the browser called moment.js.Flask-Moment is an extension for Flask applications that intergrates moment.js in jinja2 templates"""
# pip install flask-moment
from flask import Flask, render_template
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
moment = Moment(app)


@app.route('/')
def index():
    current_time = datetime.now()
    return render_template('index.html', current_time=current_time)


if __name__ == '__main__':
    app.run()
