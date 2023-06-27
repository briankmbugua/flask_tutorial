from flask import Flask
from flask.ext.script import Manager

app = Flask('__main__')

manager = Manager(app)
@app.route('/')
def index():
    return '<h1>hello</h1>'

if __name__ == "__main__":
    #app.run(debug=True)
    manager.run()
