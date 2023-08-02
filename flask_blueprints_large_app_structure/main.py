from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from blueprints.helloworld.helloworld import helloworld_bp
from blueprints.calculator.calculator import calculator_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'pymysql+mysql://root/password@localhost:3306/usersdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.register_blueprint(helloworld_bp)
app.register_blueprint(calculator_bp, url_prefix="/calculator")

if __name__ == '__main__':
    app.run(debug=True)
