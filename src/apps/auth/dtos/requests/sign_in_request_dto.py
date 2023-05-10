import marshmallow as ma
from marshmallow import validate, Schema


class SignInRequestDto(Schema):
    email = ma.fields.Email(required=True, validate=validate.Email)
    password = ma.fields.String(required=True, validate=validate.Length(min=6))
