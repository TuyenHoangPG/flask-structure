from commons.middlewares.validation_middleware import valid_schema
from flask import Blueprint

from .dtos.requests import SignUpRequestDto, SignInRequestDto
from .dtos.responses import SignUpResponseDto
from .auth_service import AuthService
from flask_apispec import marshal_with

auth_route = Blueprint("auth", __name__, url_prefix="/auth")


class AuthController():
    auth_service = AuthService()

    @auth_route.route("/sign-up", methods=["POST"])
    @valid_schema(SignUpRequestDto)
    @marshal_with(SignUpResponseDto)
    def sign_up(self, data):
        return self.auth_service.register_user(data)

    @auth_route.route("/sign-in", methods=["POST"])
    @valid_schema(SignInRequestDto)
    def sign_in(self, data):
        return self.auth_service.sign_in(data)
