# store standard roots of website, everything that's not related to authentication

# allows us to split up views for better organization
from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/') # decorator
def home():
    return "<h1>Test</h1>"

