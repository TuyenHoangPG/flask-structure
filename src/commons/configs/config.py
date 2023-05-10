import os
from dotenv import load_dotenv, find_dotenv

env_file = find_dotenv(filename=f'.env.{os.getenv("FLASK_ENV")}')
load_dotenv(env_file)


class Config(object):
    """Base configuration."""
    SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDISTOGO_URL = os.getenv("REDIS_URI")
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 10
    CORS_ORIGIN_WHITELIST = os.getenv("CORS_ORIGIN_WHITELIST").split(sep=',')
    TOKEN_EXPIRE_HOURS = 0
    TOKEN_EXPIRE_MINUTES = 0


class ProdConfig(Config):
    """Production configuration."""
    ENV = 'prod'
    DEBUG = False
    TOKEN_EXPIRE_HOURS = 1


class UatConfig(Config):
    """UAT configuration."""
    ENV = 'uat'
    DEBUG = False
    TOKEN_EXPIRE_HOURS = 1


class DevConfig(Config):
    """Development configuration."""
    ENV = 'dev'
    DEBUG = True
    TOKEN_EXPIRE_MINUTES = 15


ENV_CONFIG_DICT = dict(
    dev=DevConfig,
    uat=UatConfig,
    prod=ProdConfig
)


def get_config(config_name):
    """Retrieve environment configuration settings."""
    return ENV_CONFIG_DICT.get(config_name, DevConfig)
