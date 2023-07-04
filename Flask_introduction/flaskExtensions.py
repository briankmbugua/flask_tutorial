"""Flask is desinged to be extended."""
# Command-line options with Flaks-Script
"""For example passing configuration files is done by passing them to app.run() call.Flask_Script is an extension for Flask that adds a command-line parser to your Flask application.It comes packaged with a set of general-purpose options and also supports custom commands.It can be installed with pip"""

from flask import Flask
app = Flask(__name__)

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello</h1>'

if __name__ == "__main__":
    app.run()


"""Extensions developed specifically for Flask are exposed under the flask.ext namespace.Flask-Script exports a class named Manager, which is imported from flask.ext.script.The method of initialization of this extension is common to many extensions:an instance of the main class is initialized by passing the application instance as an argument to the constructor.The object created is then used as appropriate for each extension.In this case, the server startup is rooted through manager.run(), where the command line is passed"""

