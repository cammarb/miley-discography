import imp
from flask import Flask
from app.models import album


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config")
    return app


# def register_blueprints(app: Flask):
#     return
