from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from schemas.guild_settings import GuildSettingsSchema
from models.guild_settings import GuildSettingsModel

guild_settings_schema = GuildSettingsSchema()


class GuildSettings(Resource):
    @classmethod
    @jwt_required(optional=True)
    def put(cls):
        if not cls.is_client_authorized():
            return cls.not_authorized_response

        guild_settings_json = request.get_json()
        guild_settings = GuildSettingsModel.find_guild_settings(guild_settings_json["guild_id"]).first()

        guild_settings = guild_settings_schema.load(guild_settings_json)

        guild_settings.save_to_db()

        return guild_settings_schema.dump(guild_settings), 200
