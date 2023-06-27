# The jinja2 Template Engine
"""In it's simplest form a Jinja2 template is a file that contains a text of a response"""

# Rendering Templates
"""By default Flask looks for templates in a templates subfolder located inside the application folder."""


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


"""The function render_template provided by Flask intergrates the jinj2 template engine with the application.This function takes the filename of the template as it's first argument.Any additional arguments are key/value pairs that represent actual values for variables referenced in the template."""
# Varibles
"""{{}} - this represents a variable this tells the template engine that the value that goes in that place should be obtained from data provided at the time the template is rendered.Jinja recognizes variables of any type
<p>A value from a dictionary: {{mydict['key']}}</p>
<p>A value from a list: {{mylist[3]}}</p>
<p>A value from a list with a variable index: {{mylist[myintvar]}}</p>
<p>A value from an object's method {{myobj.somemethod()}}</p>
Variables can be modified with filters, which are added after the variable name with a pipe character as separator. e.g show the name variable capitalized  {{name | capitalize}}
Some common filters
safe - Renders the value without applying escaping
capitalize -  Converts the first character of the value to uppercase and the rest to lowercase
lower - Converts the value to lowercase characters
upper - Converts the value to uppercase characters
title - Capitalizes each word in the value
trim - Removes leading and trailing whitespace from the value
striptags - Removes any HTML tags from the value before rendering

to highlight the safe filter - By default jinja escapes all variables for security purposes.Example '<h1>Hello</h1> jinja2 will render the string as '&lt;h1&gt;Hello&lt;/h1&gt;' which will cause the h1 element to be displayed and not interpreted by the browser To display code use the safe filter.Never use the safe filter on values that aren't trusted eg text entered by users on web forms"""
# CONTROL STRUCTURES
"""
CONDITIONAL STATEMENT

{%if user%}
    hello, {{user}}!
{% else %}
    hello Stranger!
{% endif %}

RENDERING A LIST OF ELEMENTS

<ul>
{% for comment in comments %}
     <li>{{comment}}</li>
{% endfor %}
</ul>

JINJA ALSO SUPPORTS MACROS WHICH ARE SIMILAR TO FUNCTIONS IN PYTHON CODE
{% macro render_comment(comment) %}
       <li> {{ comment }}</li>
{% endmacro %}

<ul>
      {% for comment in comments %}
          {{ render_comment(comment) }}
      {% endfor %}
</ul>

macros can also be imported

{% import 'macros.html' as macros %}

{% for comment in comments %}
    {{macros.render_comment(comment) }}
{% endfor %}

ANOTHER WAY TO REUSE CODE IS THROUGH TEMPLATE INHERITANCE, WHICH IS SIMILAR TO CLASS INHERITANCE IN PYTHON
A BASE TEMPLATE
<html>
<head>
    {% block head %}
    <title>{% block title %}{% endblock %} - My Application</title>
    {% endblock %}
</head>
{% block body %}
{% endblock %}
</body>
</html>

Here the block tags define elements that a derived template can change.

{% extends "base.html" %} # this template derives from base.html
{% block title %}Index{% endblock %}
{% block head %}
    {{ super() }} using super to retain original contents
    <style>
    </style>
{% endblock %}
{% block body %}
<h1>Hello, world!</h1>
"""


if __name__ == "__main__":
    app.run(debug=False)
