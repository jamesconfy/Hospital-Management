from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager
from config import ProdConfig

bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.category = 'info'
login_manager.refresh_view = 'relogin'
login_manager.needs_refresh_message = (u"Session timedout, please re-login")
login_manager.needs_refresh_message_category = "info"

def create_app():
    app = Flask("hospital_management")
    app.config.from_object(ProdConfig)
    bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    with app.app_context():
        from hospital_management import routes
        db.create_all()

    return app
