from ..models import User
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from ..schemas import UserSchema, LoginSchema
from flask_jwt_extended import create_access_token, \
    create_refresh_token
from passlib.hash import pbkdf2_sha256 as sha256

bp = Blueprint('auth', __name__, url_prefix='/users',
               description='Operations on users')


@bp.route('/register')
class RegisterUserResource(MethodView):
    @bp.arguments(UserSchema)
    @bp.response(201, UserSchema)
    def post(self, new_user):
        """Register a new user"""

        # convert the username and email to lowercase
        new_user.username = new_user.username.lower()
        new_user.email = new_user.email.lower()

        user = User.query.filter_by(username=new_user.username).first()
        if user:
            abort(409, message='Username already exists')
        user = User.query.filter_by(email=new_user.email).first()
        if user:
            abort(409, message='Email already exists')
        new_user.password = sha256.hash(new_user.password)
        new_user.save()
        return new_user


@bp.route('/login')
class LoginUserResource(MethodView):
    @bp.arguments(LoginSchema)
    def post(self, user):
        """Login a user"""

        # convert the email to lowercase
        user.email = user.email.lower()

        current_user = User.query.filter_by(email=user.email).first()
        if not current_user:
            abort(404, message='User not found')
        if not sha256.verify(user.password, current_user.password):
            abort(401, message='Invalid credentials')
        access_token = create_access_token(identity=user.username)
        refresh_token = create_refresh_token(identity=user.username)
        return {'access_token': access_token,
                'refresh_token': refresh_token}
