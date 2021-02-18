from flask import render_template
from flask_mail import Message

import app.config
from app import mail


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject=subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)


def send_magic_link(to_email, link):
    send_email(
        "Your magic link",
        app.config.ADMIN[0],
        [to_email],
        render_template('magic_link.txt', email=to_email, link=link),
        render_template('user_email_send.html', email=to_email, link=link),
    )
