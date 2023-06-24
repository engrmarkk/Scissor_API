from .extensions import db, migrate, jwt, api, cache
from .config import config_object
from flask import Flask, jsonify, make_response, request
from .models import User, Link, RevokedToken
from .auth import bp as auth_bp
from .views.users import bp as users_bp
from .views.url import bp as url_bp
from flask_cors import CORS


def create_app(configure=config_object['appcon']):
    app = Flask(__name__)
    app.config.from_object(configure)
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    # Enable CORS
    CORS(app, supports_credentials=True)
    cache.init_app(app)
    jwt.init_app(app)

    # @app.after_request
    # def after_request(response):
    #     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    #     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    #     response.headers.add('Access-Control-Allow-Credentials', 'true')
    #     response.headers.add('Access-Control-Allow-Origin', '*')
    #     return response

    # Before each request, add CORS headers
    @app.before_request
    def before_request():
        if request.method == 'OPTIONS':
            headers = {
                'Access-Control-Allow-Origin': 'http://localhost:3000',  # Replace with your frontend origin
                # 'Access-Control-Allow-Origin': ' https://scissor-alpha.vercel.app',  # Replace with your frontend origin
                'Access-Control-Allow-Methods': 'GET, PUT, POST, DELETE, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
                'Access-Control-Allow-Credentials': 'true'
            }
            return '', 204, headers

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )

    @jwt.additional_claims_loader
    def add_additional_claims(identity):
        if identity == 1:
            return {"is_admin": True}
        return {"is_admin": False}

    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "description": "The token is not fresh.",
                    "error": "fresh_token_required",
                }
            ),
            401,
        )

    # Callback function to check if a JWT exists in the database blocklist
    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
        jti = jwt_payload["jti"]
        token = db.session.query(RevokedToken.id).filter_by(jti=jti).scalar()

        return token is not None

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )

    api.register_blueprint(auth_bp)
    api.register_blueprint(users_bp)
    api.register_blueprint(url_bp)

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({"error": "Not found"}), 404)

    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'User': User, 'Link': Link}

    return app
