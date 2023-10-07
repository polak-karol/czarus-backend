from flask import request
from flask_jwt_extended import jwt_required

from resources.base import BaseResource
from schemas.answer_config import AnswerConfigSchema
from models.answer_config import AnswerConfigModel

answer_config_schema = AnswerConfigSchema()


class AnswerConfig(BaseResource):
    @classmethod
    @jwt_required(optional=True)
    def put(cls, guild_id: str):
        if not cls.is_client_authorized():
            return cls.not_authorized_response

        answer_config_json = request.get_json()
        answer_config_json["guild_id"] = guild_id
        answer_config_query = AnswerConfigModel.find_answer_config(guild_id)
        answer_config = answer_config_query.first()

        if answer_config:
            answer_config_query.update(cls.recursive_snake_case(answer_config_json))
        else:
            answer_config = answer_config_schema.load(cls.recursive_camelize(answer_config_json))

        answer_config.save_to_db()

        return {"data": answer_config_schema.dump(answer_config)}, 200

    @classmethod
    @jwt_required(optional=True)
    def get(cls, guild_id: str):
        if not cls.is_client_authorized():
            return cls.not_authorized_response

        answer_config = AnswerConfigModel.find_answer_config(guild_id).first()

        return {"data": answer_config_schema.dump(answer_config)}, 200


class AnswerConfigList(BaseResource):

    @classmethod
    @jwt_required(optional=True)
    def get(cls):
        if not cls.is_client_authorized():
            return cls.not_authorized_response

        answer_config = AnswerConfigModel.get_all_config()

        return {"data": answer_config_schema.dump(answer_config, many=True)}, 200
