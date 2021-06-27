# store standard roots of website, everything that's not related to authentication

# allows us to split up views for better organization
from flask import Blueprint, render_template
from flask_login import login_required, current_user


views = Blueprint('views', __name__)

@views.route('/') # decorator
@login_required
def home():
    return render_template("home.html", user=current_user) # reference current user to see if authenticated

