from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user

from app import db
from app.models import Article

posts_bp = Blueprint('posts', __name__, url_prefix='/posts')


@posts_bp.route("")
def posts():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template('posts.html', articles=articles, user_is_authenticated=current_user.is_authenticated)


@posts_bp.route("/<int:id>")
def post_detail(id):
    article = Article.query.get(id)
    return render_template('post_detail.html', article=article, user_is_authenticated=current_user.is_authenticated)


@posts_bp.route("/<int:id>/delete")
@login_required
def post_delete(id):
    article = Article.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect(url_for('posts.posts'))
    except:
        return "Oops.. an error occurred while deleting an article"


@posts_bp.route("/<int:id>/update", methods=['POST', 'GET'])
@login_required
def post_update(id):
    article = Article.query.get(id)

    if request.method == 'POST':
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']

        try:
            db.session.commit()
            flash('Article is updated successfully', 'alert-success')
            return redirect(url_for('posts.posts'))
        except:
            return "Oops.. an error occurred while updating article"

    return render_template('post_update.html', article=article)
