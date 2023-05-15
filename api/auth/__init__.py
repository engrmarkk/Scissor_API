from flask import jsonify
from ..models import User, RevokedToken
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from ..schemas import UserSchema, LoginSchema
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
    get_jwt,
)
from ..utils import check_if_email_is_unique, check_if_username_is_unique
from passlib.hash import pbkdf2_sha256 as sha256
from datetime import timedelta
from ..extensions import cache

bp = Blueprint("auth", __name__, description="Operations on users")


@bp.route("/register")
class RegisterUserResource(MethodView):
    @bp.arguments(UserSchema)
    @bp.response(201, UserSchema)
    def post(self, new_user):
        """Register a new user"""
        # check if the username and email are unique
        check_if_username_is_unique(new_user["username"].lower())
        check_if_email_is_unique(new_user["email"].lower())
        if new_user["password"] != new_user["confirm_password"]:
            abort(400, message="Passwords do not match")
        password = sha256.hash(new_user["password"])
        user = User(
            username=new_user["username"].lower(),
            email=new_user["email"].lower(),
            first_name=new_user["first_name"].lower(),
            last_name=new_user["last_name"].lower(),
            password=password,
        )
        user.save()
        return user


@bp.route("/refresh")
class TokenRefresh(MethodView):
    # jwt_required simply means a token will be required to access this route
    # for you to generate a token, you need too login first
    @bp.doc(
        description="Refresh an access token",
        summary="Refresh an access token using a refresh token",
    )
    @jwt_required(refresh=True)
    def post(self):
        # get the current user's id, use it as an identity to create a new access token using the refresh token
        current_user = get_jwt_identity()
        new_token = create_access_token(
            identity=current_user, expires_delta=timedelta(hours=2)
        )

        # return the new generated token
        return {"access_token": new_token}


@bp.route("/login")
class LoginUserResource(MethodView):
    @bp.arguments(LoginSchema)
    def post(self, user):
        """Login a user"""
        current_user = User.query.filter_by(email=user["email"].lower()).first()
        if not current_user:
            abort(404, message="User not found")
        if not sha256.verify(user["password"], current_user.password):
            abort(401, message="Invalid password")
        access_token = cache.get(current_user.id)
        if not access_token:
            access_token = create_access_token(identity=current_user.id)
            cache.set(current_user.id, access_token, timeout=None)
        refresh_token = create_refresh_token(identity=current_user.id)
        return {"access_token": access_token, "refresh_token": refresh_token}


@bp.route("/logout", methods=["DELETE"])
@bp.doc(
    description="Logout a user", summary="Logout a user by revoking their access token"
)
@jwt_required()
def revoke_auth():
    jti = get_jwt()["jti"]
    current_user = get_jwt_identity()
    cached_data = cache.get(current_user)
    if cached_data:
        cache.delete(current_user)
    token = RevokedToken(jti=jti)
    token.save()
    return jsonify(msg="Successfully logged out")
