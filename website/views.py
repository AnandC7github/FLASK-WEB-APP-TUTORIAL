# views.py
from flask import Blueprint, render_template
from flask_login import current_user  # Import current_user from Flask-Login

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", user=current_user)
