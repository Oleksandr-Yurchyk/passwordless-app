from datetime import datetime

from flask_login import UserMixin

from . import db


class User(db.Model, UserMixin):
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, unique=True)
    magic_link_count = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.id


class Article(db.Model):
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    author = db.Column(db.String(100))

    def __repr__(self):
        return '<Article %r>' % self.id
