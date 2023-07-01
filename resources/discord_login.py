from flask import request
import requests
from flask_jwt_extended import create_refresh_token, create_access_token

from db import db_session
from resources.base import BaseResource
from models.user import UserModel
from schemas.user import UserSchema

user_schema = UserSchema()
dump_user_schema = UserSchema(
    only=["id", "username", "email", "avatar", "locale", "discord_access_token"]
)


class DiscordLogin(BaseResource):
    _administrator_permission = 8

    @classmethod
    def post(cls):
        user_json = request.get_json()
        data = {
            "client_id": 993578103538458664,
            "client_secret": "6erHxpCwT3pJQNpwz1oVNbELUxY7By1g",
            "grant_type": "authorization_code",
            "code": user_json["code"],
            "redirect_uri": "http://localhost:5173/authorize",
            "scope": "identify guilds email",
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response_oauth = requests.post(
            "https://discord.com/api/oauth2/token", data=data, headers=headers
        )

        if response_oauth is None:
            error_response = {
                "error": request.args["error"],
                "error_description": request.args["error_description"],
            }
            return error_response

        tokens = response_oauth.json()
        response_user = None

        if "access_token" in tokens:
            discord_access_token = tokens["access_token"]
            response_user = requests.get(
                "https://discordapp.com/api/users/@me",
                headers={"Authorization": f"Bearer {discord_access_token}"},
            )

        if response_user is None:
            error_response = {
                "error": request.args["error"],
                "error_description": request.args["error_description"],
            }
            return error_response

        discord_user = response_user.json()
        discord_user["discord_access_token"] = discord_access_token
        user_query = UserModel.find_by_id(discord_user["id"])
        user = user_query.first()

        if user:
            user_query.update(cls.t_dict(discord_user))
        else:
            user = user_schema.load(discord_user, session=db_session)

        user.save_to_db()

        access_token = create_access_token(identity=user.id, fresh=True, expires_delta=False)
        refresh_token = create_refresh_token(user.id)

        reg = requests.get(
            "https://discordapp.com/api/users/@me/guilds",
            headers={"Authorization": f"Bearer {tokens['access_token']}"},
        )
        guilds_response = reg.json()

        if 'global' in guilds_response:
            error_response = {
                "error": request.args["error"],
                "error_description": request.args["error_description"],
            }
            return error_response

        return {
            "data": {
                "accessToken": access_token,
                "refreshToken": refresh_token,
                "user": dump_user_schema.dump(user),
                "guilds": cls._format_guilds_with_administrator_permission(guilds_response),
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
        if not guilds:
            return guilds

        return [
            guild
            for guild in guilds
            if cls._is_guild_administrator(guild["permissions_new"])
        ]
