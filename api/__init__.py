from .extensions import db, migrate, jwt
from .config import AppConfig
from flask import Flask


def create_app(config_object=AppConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    return app
