from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from .admin_page import admin_page

nested_page = Blueprint('nested_page', __name__, template_folder='templates')


@nested_page.route('/', defaults={'page': 'index'})
@nested_page.route('/<page>')
def show_nested(page):
    try:
        return render_template(f'nested_pages/{page}.html')
    except TemplateNotFound:
        abort(404)

# Register the admin_page blueprint within the nested_page blueprint


nested_page.register_blueprint(admin_page, url_prefix='/admin')
