import unittest
from ..extensions import db
from ..config import config_object
from .. import create_app
from ..models import User
from passlib.hash import pbkdf2_sha256 as sha256


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_object["testcon"])
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()
        user = User(
            first_name="john",
            last_name="doe",
            username="johndoe",
            email="doejoe@yahoo.com",
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

    def test_user_registration(self):
        # test for user registration
        data = {
            "first_name": "john",
            "last_name": "doe",
            "username": "johndoe2",
            "email": "johndoe@yahoo.com",
            "password": "password",
            "confirm_password": "password",
        }
        response = self.client.post("/register", json=data)
        user = User.query.filter_by(email=data["email"]).first()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(user.first_name, data["first_name"])
        self.assertEqual(user.last_name, data["last_name"])
        self.assertEqual(user.email, data["email"])

    def test_user_login(self):
        # test for user login
        data = {
            "email": "doejoe@yahoo.com",
            "password": "password",
        }
        response = self.client.post("/login", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.json)

    def test_get_all_users(self):
        # test for getting all users
        response = self.client.get("/users")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
