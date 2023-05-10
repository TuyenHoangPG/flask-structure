from functools import wraps

from flask import request
from marshmallow import ValidationError
from marshmallow.validate import Validator

from commons.exceptions import ApiException


def valid_schema(schema):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            json_data = request.get_json()
            try:
                result, errors = schema().load(json_data)
                if errors:
                    raise ApiException(message=errors, status_code=400)
            except ValidationError as error:
                raise ApiException(message=error.messages, status_code=400)

            return func(data=json_data, *args, **kwargs)

        return wrapper

    return decorator
