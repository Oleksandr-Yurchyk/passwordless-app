import datetime
import secrets

from flask import Blueprint, render_template, redirect, request, url_for, flash, session
from flask_login import login_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

import app.config
from app import db
from app import login_manager
from app.emails import send_magic_link
from app.models import User

login_bp = Blueprint('login', __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@login_bp.route("/login", methods=["POST", "GET"])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for(f'profile.profile', username=current_user.username))

    if request.method == 'POST':
        username_or_email = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username_or_email).first()
        user_by_email = User.query.filter_by(email=username_or_email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)

                return redirect(url_for('profile.profile', username=current_user.username))
            else:
                flash('User detected, but wrong password', 'alert-danger')
        elif user_by_email:
            if check_password_hash(user_by_email.password, password):
                login_user(user_by_email)

                next_page = request.args.get('next')
                if next_page:
                    return redirect(next_page)
                return redirect(url_for('profile.profile', username=current_user.username))
            else:
                flash('User detected, but wrong password', 'alert-danger')
        else:
            flash('No such user with that name', 'alert-danger')
    return render_template('login.html')


@login_bp.route("/login_passwordless", methods=["POST", "GET"])
def login_passwordless_page():
    # Check if user is_authenticated then redirect to profile page
    if current_user.is_authenticated:
        return redirect(url_for(f'profile.profile', username=current_user.username))

    if request.method == 'POST':
        email = request.form['email']

        # If user exist in db - continue, otherwise flash message
        user = User.query.filter_by(email=email).first()
        if user:
            # Generate token
            token = secrets.token_hex(20)

            # Create magic link
            magic_link = f'{app.config.LOCAL_HOST}/login_passwordless/{token}/{user.username}'
            try:
                # Send message to users email
                send_magic_link(user.email, magic_link)

                # Save token and expires time in session
                session['token'] = token
                session['token_expires'] = datetime.datetime.utcnow() + datetime.timedelta(
                    minutes=app.config.TOKEN_TIME_EXPIRED_IN_MIN)
            except:
                flash('Something went wrong while sending email', 'alert-danger')
                return render_template('login_passwordless.html')

            flash('We sent you email! To authorized, please, go check it', 'alert-success')
            return render_template('login_passwordless.html')
        else:
            flash('No such user with that email', 'alert-danger')

    return render_template('login_passwordless.html')


@login_bp.route("/login_passwordless/<string:token>/<string:username>", methods=["GET"])
def login_page_token(token, username):
    # Check if token not expired
    if session['token_expires'] > datetime.datetime.utcnow():
        # Check if token is correct
        if session['token'] == token:
            user = User.query.filter_by(username=username).first()
            if user:
                # Reset magic link counter if it is great or equal 10
                if user.magic_link_count >= 10:
                    reset_magic_link_counter_for(username)

                # Increment magic link counter by 1
                user.magic_link_count += 1
                db.session.commit()

                login_user(user)
                return redirect(url_for('profile.profile', username=username))
            else:
                flash("Invalid user", 'alert-danger')
                return redirect(url_for('login.login_passwordless_page'))
        else:
            flash("Invalid token", 'alert-danger')
            return redirect(url_for('login.login_passwordless_page'))
    else:
        flash("Sorry your token has been expired", 'alert-danger')
        return redirect(url_for('login.login_passwordless_page'))


def reset_magic_link_counter_for(username):
    user = User.query.filter_by(username=username).first()

    user.magic_link_count = 0
    db.session.commit()


@login_bp.route("/signup", methods=["POST", "GET"])
def signup_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # Check validation: length of username & password should be great of equal 3
        if len(username) <= 2 and len(email) <= 5 and len(password) <= 2:
            flash('Fields are filled incorrect', 'alert-danger')
            return render_template('signup.html')

        else:
            # Find count of users with given username
            user_count = User.query.filter_by(username=username).count()
            if user_count == 0:
                # Adding new user to db
                hashed_pass = generate_password_hash(password)
                new_user = User(username=username, password=hashed_pass, email=email, magic_link_count=0)

                try:
                    db.session.add(new_user)
                    db.session.commit()
                    flash('Signup have been done successfully', 'alert-success')
                    return redirect(url_for('login.login_passwordless_page'))
                except Exception as e:
                    db.session.rollback()
                    flash(f"Oops.. some error occurred while adding user to db", 'alert-danger')
                    print(e)
                    return render_template('signup.html')
            else:
                # Username already exist in db
                flash(f"Seems like user with that name already exist", 'alert-danger')
                return render_template('signup.html')
    else:
        return render_template('signup.html')
