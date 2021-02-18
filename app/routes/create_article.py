from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

from app import db
from app.models import Article

create_article_bp = Blueprint('create_article', __name__, url_prefix='/posts')


@create_article_bp.route("/create_article", methods=['POST', 'GET'])
@login_required
def create_article():
    if request.method == 'POST':
        if len(request.form['title']) <= 2:
            flash('Too small title! Length of title should be least 3 character.', 'alert-danger')

        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        author = current_user.username

        article = Article(title=title, intro=intro, text=text, author=author)

        try:
            db.session.add(article)
            db.session.commit()
            flash('Article is created successfully', 'alert-success')
            return redirect(url_for('posts.posts'))
        except Exception as e:
            print(e)
            return "Oops.. an error occurred while adding article"

    return render_template('create_article.html')
