from flask import Blueprint, Flask
from src.commons.extensions import bcrypt, cache, db, migrate, jwt, cors
from src.apps import user
from src.commons.exceptions import ApiException
from src.commons.configs.config import get_config


def create_app(config_name):
    app = Flask(__name__.split('.')[0])
    app.url_map.strict_slashes = False
    app.config.from_object(get_config(config_name))

    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)

    return app


def register_extensions(app):
    """Register Flask extensions."""
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)


def register_blueprints(app):
    """Register Flask blueprints."""
    origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')
    api = Blueprint("api", __name__, url_prefix="/api")
    api.register_blueprint(user.user_controller.user_route)

    cors.init_app(api, origins=origins)
    app.register_blueprint(api)


def register_errorhandlers(app):

    def errorhandler(error):
        response = error.to_json()
        # response.status_code = error.status_code
        return response

    app.errorhandler(ApiException)(errorhandler)
