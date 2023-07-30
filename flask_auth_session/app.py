from flask import Flask, render_template, request, session, redirect
from flask_session import Session


app = Flask(__name__)
app.config["SECRECT_KEY"] = 'Codingninjas'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def welcome():
    # check if the user exists or not
    if not session.get("user_name"):
        # if the username isn't found, the page will be redirect to the login page
        return redirect("/login")
    return render_template('welcome.html', session=session)


@app.route("/login", methods=["POST", "GET"])
def login():
    # If form is submitted
    if request.method == "POST":
        # Record the user from the login.html
        session["user_name"] = request.form.get("name")
        # Redirect to the main page
        return redirect("/")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session["user_name"] = None
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
