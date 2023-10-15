from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required

import requests
from resources.base import BaseResource
from models.user import UserModel
from schemas.user import UserSchema

user_schema = UserSchema()
dump_user_schema = UserSchema(
    only=[
        "id",
        "username",
        "email",
        "avatar",
        "locale",
        "global_name",
        "banner",
        "accent_color",
        "verified",
        "flags",
        "premium_type",
        "discord_access_token",
    ]
)


class User(BaseResource):
    _administrator_permission = 8

    @classmethod
    @jwt_required()
    def get(cls):
        user_id = get_jwt_identity()
        user = UserModel.find_by_id(user_id).first()

        if not user:
            error_response = {
                "error": request.args["error"],
                "error_description": request.args["error_description"],
            }
            return error_response

        guilds_response = requests.get(
            "https://discordapp.com/api/users/@me/guilds",
            headers={"Authorization": f"Bearer {user.discord_access_token}"},
        )
        guilds_response_json = guilds_response.json()

        if "global" in guilds_response_json or "message" in guilds_response_json:
            error_response = {
                "error": request.args["error"],
                "error_description": request.args["error_description"],
            }
            return error_response

        return {
            "data": {
                "user": dump_user_schema.dump(user),
                "guilds": cls.recursive_camelize(
                    cls._format_guilds_with_administrator_permission(
                        guilds_response_json
                    )
                ),
            }
        }, 200

    @classmethod
    def _is_guild_administrator(cls, permissions: int):
        return (
                permissions & cls._administrator_permission == cls._administrator_permission
        )

    @classmethod
    def _format_guilds_with_administrator_permission(cls, guilds: bytearray):
        if not guilds:
            return guilds

        return [
            guild
            for guild in guilds
            if cls._is_guild_administrator(int(guild["permissions_new"]))
        ]
