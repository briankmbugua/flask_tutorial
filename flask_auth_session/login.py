from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)


# Since the session information will be encrypted on the server we need to provide flask with a secret key that it can use to encrypt the data
app.config['SECRET_KEY'] = "hello"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

# creating session data, Sessions are represented in python as dictionaries.This means we can access values using keys.To save a new value in a session just create a new dictionary key and assing it a value
# session["my key"] = "my value"


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True  # <--- make the permanent session
        user = request.form["name"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")


# Now from our /user page we can display the users name by simply grabbing the information from the session.If they have not singed in yet we will see that they have no username in their session and we can redirect them to the login page
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))


# When a user goes to /logout we need to clear their session data.To do this we can use a method called session.pop("key", what to do if key doesn't exist).The pop method will try to remove and return the key from the session data and will return the second argument if the key doesn't exist.
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# session duration
# by default a session lasts as long as your browser is open.However there is a way to change that from flask.We can set the duration of a session by creating a permanent session.Creating a permanent session allows us to define how long that session lasts.The default duration of a permanent session is 30 days


if __name__ == "__main__":
    app.run(debug=True)
