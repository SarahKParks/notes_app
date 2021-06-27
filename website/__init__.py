# makes website folder a python package to be able to import it

from flask import Flask

# initalize Flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1' # to encrypt session data, not for production
    
    # register Blueprints w/ location
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

