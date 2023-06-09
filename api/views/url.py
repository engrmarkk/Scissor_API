from ..models import Link
from flask import Response
from flask_smorest import abort, Blueprint
from flask import redirect, make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask.views import MethodView
from ..schemas import LinkSchema, GetLinksSchema
from ..utils.url_validate import validate_url

# from ..utils import check_if_user_is_still_logged_in
from ..extensions import db, cache, limiter


bp = Blueprint("urls", __name__, description="Operations on urls")


@bp.route("/short-urls")
class CreateShortUrl(MethodView):
    @bp.arguments(LinkSchema)
    # @bp.response(201, LinkSchema)
    @jwt_required()
    @limiter.limit("10 per minute")
    def post(self, new_url):
        """Create a new short url"""
        current_user = get_jwt_identity()
        if not validate_url(new_url["url"]):
            abort(400, message="Invalid url")
        if not new_url["url"].startswith('http://') and not new_url["url"].startswith('https://'):
            new_url["url"] = 'http://' + new_url["url"]
        if Link.query.filter_by(user_id=current_user, url=new_url["url"]).first():
            abort(400, message="URL already exists for this user")
        link = Link(**new_url, user_id=current_user)
        link.save()
        response = {
            "url": link.url,
            "short_url": f"{request.host_url}{link.short_url}",
        }
        return response, 201


@bp.route("/<short_url>")
class RedirectShortUrl(MethodView):
    @bp.response(302)
    @cache.memoize(timeout=3600)
    def get(self, short_url):
        """Redirect to the original url"""
        link = Link.query.filter_by(short_url=short_url).first()
        if not link:
            abort(404, message="Url not found")
        link.visit += 1
        db.session.commit()
        return redirect(link.url)


@bp.route("/<short_url>/qr-code")
@jwt_required()
@cache.cached(timeout=3600)
def qr_code(short_url):
    """Get the QR code for a short url"""
    link = Link.query.filter_by(short_url=short_url).first_or_404()
    if not link.qr_code:
        # If the QR code hasn't been generated yet, generate it now
        link.qr_code = link.generate_qr_code()
        db.session.commit()
    response = make_response(link.qr_code)
    response.headers.set("Content-Type", "image/jpeg")
    return response


@bp.route("/delete-url/<string:short_url>", methods=["POST"])
@jwt_required()
def delete_short_url(short_url):
    """Delete Link"""
    # if len(short_url) > 5:
    #     short_url = short_url[-5:]
    link = Link.query.filter_by(short_url=short_url).first()
    if not link:
        abort(404, message="This url does not exist")
    db.session.delete(link)
    db.session.commit()
    return Response({"message": "Deleted"})
