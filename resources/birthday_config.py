from flask import request
from flask_jwt_extended import jwt_required

from resources.base import BaseResource
from schemas.birthday_config import BirthdayConfigSchema
from models.birthday_config import BirthdayConfigModel

birthday_config_schema = BirthdayConfigSchema()


class BirthdayConfig(BaseResource):
    @classmethod
    @jwt_required(optional=True)
    def put(cls, guild_id):
        if not cls.is_client_authorized():
            return cls.not_authorized_response

        birthday_config_json = request.get_json()
        birthday_config_json["guild_id"] = guild_id
        birthday_config_query = BirthdayConfigModel.find_birthday_config(guild_id)
        birthday_config = birthday_config_query.first()

        if birthday_config:
            birthday_config_query.update(cls.recursive_snake_case(birthday_config_json))
        else:
            birthday_config = birthday_config_schema.load(cls.recursive_camelize(birthday_config_json))

        birthday_config.save_to_db()

        return {"data": birthday_config_schema.dump(birthday_config)}, 200

    @classmethod
    @jwt_required(optional=True)
    def get(cls, guild_id):
        if not cls.is_client_authorized():
            return cls.not_authorized_response

        birthday_config = BirthdayConfigModel.find_birthday_config(guild_id).first()

        return {"data": birthday_config_schema.dump(birthday_config)}, 200


class BirthdayConfigList(BaseResource):

    @classmethod
    @jwt_required(optional=True)
    def get(cls):
        if not cls.is_client_authorized():
            return cls.not_authorized_response

        birthday_config = BirthdayConfigModel.get_all_config()

        return {"data": birthday_config_schema.dump(birthday_config, many=True)}, 200
