from flask import request
import requests
import os
from flask_jwt_extended import create_refresh_token, create_access_token

from db import db_session
from resources.base import BaseResource
from models.user import UserModel
from schemas.user import UserSchema

user_schema = UserSchema()
dump_user_schema = UserSchema(
    only=["id", "username", "email", "avatar", "locale", "discord_access_token"]
)


class GuildBans(BaseResource):
    _administrator_permission = 8
    _user_properties_white_list = [
        "id",
        "username",
        "discriminator",
        "global_name",
        "display_name",
        "avatar",
        "locale",
        "public_flags",
        "email",
        "flags",
        "banner",
        "banner_color",
        "accent_color",
        "mfa_enabled",
        "premium_type",
        "avatar_decoration",
        "discord_access_token",
        "verified",
        "guild_ids",
    ]

    @classmethod
    def get(cls, guild_id):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Bot {os.getenv('DISCORD_APP_BOT_TOKEN')}"
        }

        try:
            guild_bans = requests.get(
                f"https://discord.com/api/guilds/{guild_id}/bans", headers=headers
            )
        except:
            return {
                "message": "Failed to authorize",
            }, 400

        guild_bans_json = guild_bans.json()

        return {
            "data": cls.recursive_camelize(guild_bans_json)
        }, 200
