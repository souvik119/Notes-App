from flask import Flask

def create_app():
    app = Flask(__name__)
    # in prod env do not share this key with anyone
    app.config['SECRET_KEY'] = 'cbwhberyfekj33zs'

    return app