from marshmallow import Schema, validate, ValidationError, \
    validates_schema, post_load, fields
from ..models import User


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    first_name = fields.String()
    last_name = fields.String()
    email = fields.Email(required=True)
    password = fields.String(required=True, load_only=True)
    confirm_password = fields.String(load_only=True, required=True)


class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, load_only=True)

    @validates_schema
    def validate_password(self, data, **kwargs):
        if not data['password']:
            raise ValidationError('Password is required')

    @validates_schema
    def validate_email(self, data, **kwargs):
        if not data['email']:
            raise ValidationError('Email is required')
