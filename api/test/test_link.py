import unittest
from ..extensions import db
from ..config import config_object
from .. import create_app
from ..models import User, Link
from passlib.hash import pbkdf2_sha256 as sha256
from flask_jwt_extended import create_access_token


class LinkTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_object["testcon"])
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()
        user = User(
            first_name="mark",
            last_name="zack",
            username="marc_zack",
            email="mark_zarc@yahoo.com",
            password=sha256.hash("password")
        )
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        self.app = None
        self.client = None

    def test_create_short_link(self):
        # test for creating a short link
        data = {
            "url": "https://www.google.com",
        }

        # create JWT token for authorization
        token = create_access_token(identity=1)

        # set headers with JWT token
        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = self.client.post("/short-urls", json=data, headers=headers)
        self.assertEqual(response.status_code, 201)
        self.assertIn("short_url", response.json)
