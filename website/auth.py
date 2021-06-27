from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST']) # type of requests this root can accept, GET by default
def login():
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if len(email) < 4:
            flash('Invalid Email', category='error')
        elif len(first_name) < 1:
            flash('No Name Entered', category='error')
        elif len(password) < 7:
            flash('Password Too Short', category='error')
        elif password != confirm_password:
            flash('Passwords Don\'t Match', category='error')
        else:
            flash('Accounted Created', category='success')

    return render_template("sign_up.html")
