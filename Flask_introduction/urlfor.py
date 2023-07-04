from flask import Flask, url_for, render_template, redirect


# initialize the app
app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('sportsmain.html')


# view function for URL 'localhost:5000/sport/cricket/kenya'
@app.route('/cricket/<favteam>')
def cricket(favteam):
    return render_template('cricket.html', fav=favteam)


# view function for URL 'localhost:5000/sport/cricket/kenya'
@app.route('/baseball/<favteam>')
def baseball(favteam):
    return render_template('baseball.html', fav=favteam)


# Logic to decide which template to call based on 'name' variable
# The team variable will be passed to the appropriate view function
# url_for method here calls the appropriate view function and passes the parameter required

@app.route('/sport/<name>/<team>')
def game(name, team):
    # if sport is cricket call the view function for same and pass team name
    if name == 'baseball':
        return redirect(url_for('cricket', favteam=team))
    elif name == 'cricket':
        # if sport is baseball call the view function for same and pass the team name
        return redirect(url_for('baseball', favteam=team))
    else:
        # If the game page is not present return workingprogress webpage
        return render_template('workingprogress.html', sportname=name)


if __name__ == '__main__':
    app.run(debug=True)
