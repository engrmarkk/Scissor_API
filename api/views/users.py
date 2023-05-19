from ..models import User, Link
from flask_smorest import abort, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask.views import MethodView
from ..schemas import UserSchema
from ..extensions import cache

bp = Blueprint("users", __name__, description="Operations on users")


@bp.route("/users")
class UsersResource(MethodView):
    @bp.response(200, UserSchema(many=True))
    # @jwt_required()
    # @cache.cached(timeout=3600)
    def get(self):
        """Get all users"""
        users = User.query.all()
        cache.set("users", users, timeout=3600)
        return users


@bp.route("/dashboard")
class DashboardResource(MethodView):
    @bp.response(200, UserSchema)
    @jwt_required()
    def get(self):
        """Get the current user's dashboard"""
        current_user = get_jwt_identity()
        user = User.query.filter_by(id=current_user).first_or_404()
        return user
