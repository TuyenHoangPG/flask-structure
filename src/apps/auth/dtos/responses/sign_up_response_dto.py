import marshmallow as ma
from marshmallow import Schema


class SignUpResponseDto(Schema):
    id = ma.fields.String()
    email = ma.fields.Email()
    token = ma.fields.String()
    first_name = ma.fields.String()
    last_name = ma.fields.String()
