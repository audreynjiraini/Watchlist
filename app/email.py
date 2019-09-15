from flask_mail import Message # import Message class
from flask import render_template
from . import mail # import mail instance from the application factory module


def mail_message(subject, template, to, **kwargs):
    sender_email = "audreywncode@gmail.com"
    
    email = Message(subject, sender = sender_email, recipients=[to])
    email.body = render_template(template + ".txt", **kwargs)
    email.html = render_template(template + ".html", **kwargs)
    mail.send(email)