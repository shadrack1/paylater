from flask import Blueprint, render_template
from flask import current_app as current_app

auth_pg = Blueprint('auth_pg', __name__, template_folder='templates', static_folder='static')


@auth_pg.route('/signup')
def signup():
    return render_template('/signup.html')
