# Forms
"""Are the core cointainer for WTForms.Form represent a collection of fields,which can be accessed on the form dictionary-style or attribute style"""
# Fields
"""Each field represents a data type and the field handles coercing form input to that datatype.For example IntegerField and StringField represent two different data types.Fields contain a number of useful properties such as label, description, and a list of validation errors, in addition to the data the field contains
Every field has a Widget instance.The widget's job is rendering an HTML representation of that field.Some fields are simply conveniences, for example TextAreaField is simply a StringField with the defaul widget being text area"""
# validators
"""In order to specify validation rules, fields contain a list of Validators"""

# DEFINING A FORM




from wtforms import Form, BooleanField, StringField, DateTimeField, TextAreaField, IntegerField, PasswordField, validators
class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=5)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    accept_rules = BooleanField('I accept the site rules', [
                                validators.InputRequired()])


"""Because forms are regular Python classes, they can be easily extended"""


class ProfileForm(Form):
    birthday = DateTimeField('Your Birthday', format="%m/%d/%y")
    signature = TextAreaField('Forum Signature')


class AdminProfileForm(ProfileForm):
    username = StringField(
        'Username', [validators.Length(max=40)], default='brian')
    level = IntegerField(
        'User Level', [validators.NumberRange(min=0, max=10)], default=34)


"""Via subclassing, AdminProfileForm gains all the fields already defined in ProfileForm. This allows you to easily share common subsets of fields between forms"""

form = AdminProfileForm()
print(form)
# can be accessed using dictionary style or dot like object atributes
print(form.username)
print(form['level'])

print(form.username.data)
print(form['level'].data)

# When there are validators first print statement will return True and the errors will return the error it there is any
print(form.validate())
print(form.errors)

# Rendering Fields
"""Rendring a field is as simple as coercing it to a string"""
print(str(form.username)
      )  # <input id="username" maxlength="40" name="username" type="text" value="brian">


# Rendering Forms

class LoginForm(Form):
    username = StringField('Username')
    password = PasswordField('Password')
