from flask import request
from flask_jwt_extended import jwt_required

from resources.base import BaseResource
from schemas.holiday_config import HolidayConfigSchema
from models.holiday_config import HolidayConfigModel

holiday_config_schema = HolidayConfigSchema()


class HolidayConfig(BaseResource):
    @classmethod
    @jwt_required(optional=True)
    def put(cls, guild_id):
        if not cls.is_client_authorized():
            return cls.not_authorized_response

        holiday_config_json = request.get_json()
        holiday_config_json["guild_id"] = guild_id
        holiday_config_query = HolidayConfigModel.find_holiday_config(guild_id)
        holiday_config = holiday_config_query.first()

        if holiday_config:
            holiday_config_query.update(cls.recursive_snake_case(holiday_config_json))
        else:
            holiday_config = holiday_config_schema.load(cls.recursive_camelize(holiday_config_json))

        holiday_config.save_to_db()

        return {"data": holiday_config_schema.dump(holiday_config)}, 200

    @classmethod
    @jwt_required(optional=True)
    def get(cls, guild_id):
        if not cls.is_client_authorized():
            return cls.not_authorized_response

        holiday_settings = HolidayConfigModel.find_holiday_config(guild_id).first()

        return {"data": holiday_config_schema.dump(holiday_settings)}, 200


class HolidayConfigList(BaseResource):

    @classmethod
    @jwt_required(optional=True)
    def get(cls):
        if not cls.is_client_authorized():
            return cls.not_authorized_response

        holiday_config = HolidayConfigModel.get_all_config()

        return {"data": holiday_config_schema.dump(holiday_config, many=True)}, 200
