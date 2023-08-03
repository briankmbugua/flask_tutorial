from flask import Flask
from yourapplication.nested_page import nested_page
from yourapplication.simple_page import simple_page
app = Flask(__name__)


app.register_blueprint(nested_page, url_prefix='/nested')
app.register_blueprint(simple_page, url_prefix='/pages')

if __name__ == "__main__":
    app.run(debug=True)
