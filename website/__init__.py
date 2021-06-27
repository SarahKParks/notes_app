# makes website folder a python package to be able to import it

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

# initalize Flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1' # to encrypt session data, not for production
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # sqlite database stored at this location
    db.init_app(app) # initialize db with Flask app

    # register Blueprints w/ location
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    # where should we go if the user is not logged in and a login is required
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # tell flask how we load a user
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    # if database doesn't exist
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')