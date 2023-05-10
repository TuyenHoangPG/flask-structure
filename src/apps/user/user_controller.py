from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from src.commons.constants.constant import ROLES
from src.commons.middlewares.role_middleware import valid_roles
from .user_service import UserService

user_route = Blueprint("users", __name__, url_prefix="/users")


class UserController():
    user_service = UserService()

    @user_route.route("/", methods=["GET"])
    @jwt_required
    @valid_roles([ROLES.ADMIN])
    def get_list_user(self, **kwargs):
        args = request.args
        page = int(args.get("page", 1))
        item_per_page = int(args.get("itemPerPage", 5))
        total, items = self.user_service.get_list(page, item_per_page)

    @user_route.route("/<id>", methods=["PUT"])
    @jwt_required
    @valid_roles([ROLES.ADMIN, ROLES.IMAGE_REVIEWER])
    def update_user(id, **kwargs):
        user = kwargs.get("user")
        json_data = request.json
        data_update = {
            "id": id,
            "first_name": json_data.get("first_name"),
            "last_name": json_data.get("last_name"),
            "password": json_data.get("password"),
        }

        # try:
        #     is_updated = user_controller.update(user, data_update)
        # except PermissionError as e:
        #     return forbidden(str(e))

        # return success({"is_updated": is_updated})
