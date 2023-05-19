from marshmallow import Schema, fields, post_dump
from flask import request


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

    @post_dump(pass_many=True)
    def add_host_url(self, data, many, **kwargs):
        host_url = request.host_url  # Get the host URL from the request
        if many:
            # If serializing multiple objects, update each object's short_url field
            for obj in data:
                obj['short_url'] = host_url + obj['short_url']
        else:
            # If serializing a single object, update its short_url field
            data['short_url'] = host_url + data['short_url']
        return data
