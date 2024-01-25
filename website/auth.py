# auth.py
from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route("/hello")
def hello():
    return "<h1>Hello from Auth Blueprint!</h1>"
