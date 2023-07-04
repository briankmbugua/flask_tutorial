from flask import Flask, render_template
from wtforms import StringField, SubmitField


# Define a form class using WTForms.This class will inherit from FlaskForm

from flask_wtf import FlaskForm


class MyForm(FlaskForm):
    name = StringField('Name')
    email = StringField('Email')
    submit = SubmitField('Submit')


app = Flask(__name__)

app.secret_key = 'Your_secret_key'  # required for CSRF proctection


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if form.validate_on_submit():
        # Form was submitted and is valid
        # Acces form data using form.name.data, form.email.data, etc.
        return 'Form submitted succesfully'
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
