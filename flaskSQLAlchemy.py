from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configuring the database
# this is the only required configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/mydatabase'
db.init_app(app)

"""The db object gives you access to the db.Model class to define models, and the db.session to execute queries"""

# Define models
"""Subclass db.Model to define a model class.The db object makes the names in sqlachemy and sqlalchemy.orm available for convenience, such as db.Column.The model will generate a table named by converting the CamelCase class name to snake_case """


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255))


"""The table name 'user' will automatically be assinged to the model's table."""
# Creating the Tables
"""call SQLAlchemy.create_all() to create the table schema in the database.This requires an application context.Since you're not in a request at this point, create one manually"""
with app.app_context():
    db.create_all()

"""create_all does not update tables if they are already in the database.If you change a model's columns, use a migration library like Alembic with Flask-Alembic or Flask-Migrate to generate migrations that update the database schema
SQLAlchemy automatically defines an __init__ method for each models that assings any keyword arguments to the corresponding database columns and other attributes.
db.session.add(obj) -- adds an object to the session to be inserted.
db.session.delete(obj) -- deletes an object
db.session.commit() -- call this after modifying, adding or deleting any data
db.session.execute(db.select(...)) -- construct a query to select data from the database."""


# LIST ALL USERS
@app.route("/users")
def user_list():
    users = db.session.execute(
        db.select(User).order_by(User.username)).scalars()
    return render_template('user/list.html', users=users)


# CREATE A USER
@app.route("/users/create", methods=['GET', 'POST'])
def user_create():
    if request.method == 'POST':
        user = User(
            username=request.form['username'],
            email=request.form['email']
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("user_detail", id=user.id))
    return render_template("user/create.html")


@app.route('/user/<int:id>')
def user_detail(id):
    user = db.get_or_404(User, id)
    return render_template("user/detail.html", user=user)


@app.route("/user/<int:id>/delete", methods=["GET", "POST"])
def user_delete(id):
    user = db.get_or_404(User, id)
    if request.method == "POST":
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for("user_list"))
    return render_template("user/delete.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)
