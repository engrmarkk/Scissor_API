from ..models import User
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from ..schemas import UserSchema, LoginSchema
from flask_jwt_extended import create_access_token, \
    create_refresh_token
from ..utils import check_if_email_is_unique, check_if_username_is_unique
from passlib.hash import pbkdf2_sha256 as sha256

bp = Blueprint('auth', __name__, description='Operations on users')


@bp.route('/register')
class RegisterUserResource(MethodView):
    @bp.arguments(UserSchema)
    @bp.response(201, UserSchema)
    def post(self, new_user):
        """Register a new user"""
        # check if the username and email are unique
        check_if_username_is_unique(new_user.username.lower())
        check_if_email_is_unique(new_user.email.lower())
        new_user.password = sha256.hash(new_user.password)
        new_user.save()
        return new_user


@bp.route('/login')
class LoginUserResource(MethodView):
    @bp.arguments(LoginSchema)
    def post(self, user):
        """Login a user"""
        current_user = User.query.filter_by(email=user.email.lower()).first()
        if not current_user:
            abort(404, message='User not found')
        if not sha256.verify(user.password, current_user.password):
            abort(401, message='Invalid credentials')
        access_token = create_access_token(identity=user.username)
        refresh_token = create_refresh_token(identity=user.username)
        return {'access_token': access_token,
                'refresh_token': refresh_token}
