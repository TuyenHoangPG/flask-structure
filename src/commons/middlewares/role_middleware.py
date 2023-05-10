from functools import wraps

from src.commons.exceptions import ApiException
from src.commons.constants.message import ERROR_MESSSAGE


def valid_roles(list_role: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user = kwargs.get("user")

            if not user or not user.role in list_role:
                raise ApiException(
                    message=ERROR_MESSSAGE.FORBIDDEN, status_code=403)

            return func(*args, **kwargs)

        return wrapper

    return decorator
