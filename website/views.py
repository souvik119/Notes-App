# this deals with the routes on the server, i.e, home page, login page..
from flask import Blueprint

views = Blueprint('views', __name__)

# this is the url
@views.route('/')
def home():
    return '<h1>Test</h1>'