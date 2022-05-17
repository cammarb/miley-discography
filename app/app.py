import os
from flask import Flask
from app import routes
from app.extensions.database import db, migrate
from app.extensions.auth import login_manager


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config")

    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    login_manager.init_app(app)


def register_blueprints(app: Flask):
    app.register_blueprint(routes.songs.blueprint)
    app.register_blueprint(routes.albums.blueprint)
    app.register_blueprint(routes.artists.blueprint)
    app.register_blueprint(routes.static_pages.blueprint)
    app.register_blueprint(routes.auth.blueprint)
