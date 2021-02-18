from flask import Blueprint, render_template
from flask_login import current_user

about_bp = Blueprint('about', __name__)


@about_bp.route("/about")
def about():
    return render_template('about.html', user_is_authenticated=current_user.is_authenticated)
