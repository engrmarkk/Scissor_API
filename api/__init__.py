from .extensions import db, migrate, jwt, api
from .config import config_object
from flask import Flask
from .models import User, Link
from .auth import bp as auth_bp
from .views.users import bp as users_bp


def create_app(configure=config_object['appcon']):
    app = Flask(__name__)
    app.config.from_object(configure)
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    jwt.init_app(app)

    api.register_blueprint(auth_bp)
    api.register_blueprint(users_bp)

    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'User': User, 'Link': Link}

    return app
