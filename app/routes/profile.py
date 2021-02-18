from flask import Blueprint, url_for, render_template
from flask_login import login_required, logout_user
from werkzeug.utils import redirect

from app.models import User

profile_bp = Blueprint('profile', __name__)


@profile_bp.route("/profile/<username>")
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first()

    return render_template('profile.html', username=username, count=user.magic_link_count)


@profile_bp.route("/profile/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.home'))
