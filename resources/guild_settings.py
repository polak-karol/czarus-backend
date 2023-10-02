from flask import request
from flask_jwt_extended import jwt_required

from resources.base import BaseResource
from schemas.guild_settings import GuildSettingsSchema
from models.guild_settings import GuildSettingsModel

guild_settings_schema = GuildSettingsSchema()


class GuildSettings(BaseResource):
    @classmethod
    @jwt_required(optional=True)
    def put(cls, guild_id):
        if not cls.is_client_authorized():
            return cls.not_authorized_response

        guild_settings_json = request.get_json()
        guild_settings_json["guild_id"] = guild_id
        guild_settings_query = GuildSettingsModel.find_guild_settings(guild_id)
        guild_settings = guild_settings_query.first()

        if guild_settings:
            guild_settings_query.update(cls.recursive_snake_case(guild_settings_json))
        else:
            guild_settings = guild_settings_schema.load(cls.recursive_camelize(guild_settings_json))

        guild_settings.save_to_db()

        return {"data": guild_settings_schema.dump(guild_settings)}, 200

    @classmethod
    @jwt_required(optional=True)
    def get(cls, guild_id):
        if not cls.is_client_authorized():
            return cls.not_authorized_response

        guild_settings = GuildSettingsModel.find_guild_settings(guild_id).first()

        return {"data": guild_settings_schema.dump(guild_settings)}, 200


class GuildSettingsList(BaseResource):

    @classmethod
    @jwt_required(optional=True)
    def get(cls):
        if not cls.is_client_authorized():
            return cls.not_authorized_response

        guild_settings = GuildSettingsModel.get_all_settings()

        return {"data": guild_settings_schema.dump(guild_settings, many=True)}, 200
