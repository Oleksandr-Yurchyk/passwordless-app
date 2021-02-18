from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

# Globally accessible libraries
db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('./config.py')

    # Initialize plugins
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    with app.app_context():
        from .routes import home, about, create_article, login, posts, profile

        # Register Blueprints
        app.register_blueprint(home.home_bp)
        app.register_blueprint(about.about_bp)
        app.register_blueprint(create_article.create_article_bp)
        app.register_blueprint(login.login_bp)
        app.register_blueprint(posts.posts_bp)
        app.register_blueprint(profile.profile_bp)

        db.create_all()

        return app
