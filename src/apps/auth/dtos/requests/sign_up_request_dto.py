import marshmallow as ma
from marshmallow import validate, Schema


class SignUpRequestDto(Schema):
    email = ma.fields.Email(required=True, validate=validate.Email)
    password = ma.fields.String(required=True, validate=validate.Length(min=6))
    first_name = ma.fields.String(required=True)
    last_name = ma.fields.String(required=True)
