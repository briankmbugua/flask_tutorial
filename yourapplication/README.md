# Modular Applications with Blueprints
A Blueprint object works similary to a Flask application object, but it is not actually an application.Rather it is a blueprint of how to construct or extend an application

# Why Blueprints
- Factor an application into a set of blueprints.
- Register a blueprint on an application at a URL prefix and/or subdomain.
- Register a blueprint many times on an application with different URL rules.
- Provide template filters, static files, templates, and other utilities through blueprints.A blueprint does not have to implement applications or view functions.
- Register a blueprint on an application for any of these cases when initializing a Flask extension.

# yourapplication blueprint
simple_page
```python
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


simple_page = Blueprint('simple_page', __name__, template_folder='templates')


@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    try:
        return render_template(f'pages/{page}.html')
    except TemplateNotFound:
        abort(404)
```
app.py
```python
from flask import Flask
from yourapplication.simple_page import simple_page

app = Flask(__name__)

app.register_blueprint(simple_page)```
If you check the rules registered on the application, you will find these.
```bash
>>> app.url_map
Map([<Rule '/static/<filename>' (HEAD, GET, OPTIONS) -> static>,
 <Rule '/' (HEAD, GET, OPTIONS) -> simple_page.show>,
 <Rule '/<page>' (HEAD, GET, OPTIONS) -> simple_page.show>])```

 - The first one is obviously from the application itself for static files.
 - The other two are for the show function of the simple_page blueprint.They are also prefixed with the name of the bluprint and separated by a dot(.)

 Blueprints however can also be mounted at different locations
 ```python
 app.register_blueprint(simple_page, url_prefix='/pages')```
 here are the generated rules:
 ```bash
 >>> app.url_map
Map([<Rule '/static/<filename>' (OPTIONS, GET, HEAD) -> static>,
 <Rule '/pages/' (OPTIONS, GET, HEAD) -> simple_page.show>,
 <Rule '/pages/<page>' (OPTIONS, GET, HEAD) -> simple_page.show>])```

 # Nesting Blueprints
 It is possible to register a blueprint on another blueprint.

```python
parent = Blueprint('parent', __name__, url_prefix='/parent')
child = Blueprint('child', __name__, url_prefix='/child')
parent.register_blueprint(child)
app.register_blueprint(parent)```

The child blueprint will gain the parent's name as a prefix to its name, and child URLs will be pre-fixed with the parent's URL prefix

```python
url_for('parent.child.create')
/parent/child/create```

# Blueprint Resource Folder
Multiple blueprints can originate from the same folder, it does not have to be the case and it's usually not recomended.
The folder is inferred from the second argument to Blueprint which is usually __name__
You can access the Blueprint.roo_path property to see what the resource folder is
```bash
>>>name_of_blueprint.root_path```

# Static Files
A blueprint can expose a folder with static files by providing the path to the folder on the filesystem with the static_folder argument.It is either an absolute path or relative to the blueprint's location:
```python
admin = Blueprint('admin',__name__, static_folder='static')```
Because the folder is called static here it will be available at the url_prefix of the blueprint +/static.If the blueprint has the prefix /admin, the static URL will be /admin/static

The endpoint is named blueprint_name.static.You can generate URLs to it with url_for() like you would with the static folder of the application.

url_for('admin.static', filename='style.css')

if the blueprint does not have a url_prefix, it is not possible to access the blueprint's static folder.Unlike template folders, blueprint static folders are not searched if the file does not exist in the application static folder.

# Templates
If you want the blueprint to expose templates you can do that by providing the template_folder paramater to the Blueprint constructor.
```python
admin = Blueprint('admin',__name__, template_folder='templates')```
The template folder is added to the search path of templates but with a lower priority than the actual application's template folder.
If you encounter problems loading the correct templates enable the EXPLAIN_TEMPLATE_LOADING config variable which will instruct flask to print out the steps it goes through to locate templates on every render_template call.

# Building URLs
If you want to link from one page to another you can use the url_for() function just like you normally would do just that you prefix the URL endpoint with the name of the blueprint and a dot(.)

url_for('admin.index)
If you are in a view function of a blueprint or a rendered template and you want to link to another endpoint of the same blueprint, you can use relative redirects by prefixing the endpoint with a dot only.

url_for('.index')

