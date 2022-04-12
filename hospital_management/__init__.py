from flask import Flask
from config import DevConfig

def create_app():
    app = Flask("hospital_management")
    app.config.from_object(DevConfig)
    with app.app_context():
        from hospital_management import routes

    return app
