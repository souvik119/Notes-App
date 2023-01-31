from flask import Flask

def create_app():
    app = Flask(__name__)
    # in prod env do not share this key with anyone
    app.config['SECRET_KEY'] = 'cbwhberyfekj33zs'

    # Registering the views
    from .views import views
    from .auth import auth

    # these will be the prefix before actual url for the server
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app