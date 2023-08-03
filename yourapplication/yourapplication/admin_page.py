from flask import Blueprint, render_template

admin_page = Blueprint('admin_page', __name__, template_folder='templates')


@admin_page.route('/')
def admin_home():
    return render_template('nested_pages/admin/home.html')


@admin_page.route('/users')
def admin_users():
    return render_template('nested_pages/admin/users.html')
