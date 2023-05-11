from flask_jwt_extended import get_jwt_identity, jwt_required

import requests
from resources.base import BaseResource
from models.user import UserModel
from schemas.user import UserSchema

user_schema = UserSchema()
dump_user_schema = UserSchema(
    only=["id", "username", "email", "avatar", "locale", "discord_access_token"]
)


class User(BaseResource):
    _administrator_permission = 8

    @classmethod
    @jwt_required()
    def get(cls):
        user_id = get_jwt_identity()
        user = UserModel.find_by_id(user_id).first()

        reg = requests.get(
            "https://discordapp.com/api/users/@me/guilds",
            headers={"Authorization": f"Bearer {user.discord_access_token}"},
        )
        guilds = reg.json()

        return {
            "data": {
                "user": dump_user_schema.dump(user),
                "guilds": cls._format_guilds_with_administrator_permission(guilds),
            }
        }, 200

    @classmethod
    def _is_guild_administrator(cls, permissions):
        return (
            int(permissions) & cls._administrator_permission
            == cls._administrator_permission
        )

    @classmethod
    def _format_guilds_with_administrator_permission(cls, guilds):
        return [
            guild
            for guild in guilds
            if cls._is_guild_administrator(guild["permissions_new"])
        ]
