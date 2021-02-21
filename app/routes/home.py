from flask import Blueprint, render_template
from flask_login import current_user

home_bp = Blueprint('home', __name__)


@home_bp.route("/")
@home_bp.route("/home")
def home():
    if current_user.is_authenticated:
        return render_template('home.html', user_is_authenticated=True, username=current_user.username)
    return render_template('home.html')
