from flask import Flask
from app import routes
from app.extensions.database import db, migrate
from . import routes


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config")

    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app: Flask):
    app.register_blueprint(routes.songs.blueprint)
    app.register_blueprint(routes.albums.blueprint)
