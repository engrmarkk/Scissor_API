from marshmallow import Schema, fields


class LinkSchema(Schema):
    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(dump_only=True)
    url = fields.String(required=True)
    short_url = fields.String(dump_only=True)
    created_at = fields.DateTime(dump_only=True)


class GetLinksSchema(Schema):
    id = fields.Integer()
    user_id = fields.Integer()
    url = fields.String()
    short_url = fields.String()
    visit = fields.Integer()
    created_at = fields.String()
