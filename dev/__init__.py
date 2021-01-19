import datetime
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import Config


app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'load.login'
login_manager.login_message = None
login_manager.session_protection = "strong"
REMEMBER_COOKIE_NAME = 'remember_token'
REMEMBER_COOKIE_DURATION = datetime.timedelta(days=64, seconds=29156, microseconds=10)


def create_app(config_class=Config):

    db.init_app(app)
    bcrypt.init_app(app)
    ma.init_app(app)
    login_manager.init_app(app)


    from .uploads.gallery import load



    app.register_blueprint(load)


    return app
