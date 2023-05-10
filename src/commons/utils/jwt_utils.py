

from src.apps.user.user_model import User


def jwt_identity(payload):
    return User.query.filter_by(id=payload['id']).first()


def identity_loader(user):
    return user.id
