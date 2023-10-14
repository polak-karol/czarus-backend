from flask import request
from flask_jwt_extended import jwt_required

from resources.base import BaseResource
from schemas.answer import AnswerSchema
from models.answer import AnswerModel

answer_schema = AnswerSchema()


class Answer(BaseResource):
    @classmethod
    @jwt_required(optional=True)
    def get(cls, guild_id: str):
        if not cls.is_client_authorized():
            return cls.not_authorized_response

        answer = AnswerModel.find_answer(guild_id).first()

        return {"data": answer_schema.dump(answer)}, 200

    @classmethod
    @jwt_required(optional=True)
    def put(cls, guild_id: str):
        if not cls.is_client_authorized():
            return cls.not_authorized_response

        answer_json = request.get_json()
        answer_json["guild_id"] = guild_id

        answer_query = AnswerModel.find_answer(guild_id)
        answer = answer_query.first()

        if not answer:
            answer = answer_schema.load(cls.recursive_camelize(answer_json))
        else:
            answer_query.update(cls.recursive_snake_case(answer_json))

        answer.save_to_db()

        return {"data": answer_schema.dump(answer)}, 200


class AnswerList(BaseResource):
    @classmethod
    @jwt_required(optional=True)
    def get(cls, guild_id: str):
        if not cls.is_client_authorized():
            return cls.not_authorized_response

        answer = AnswerModel.find_answer(guild_id).first()

        return {"data": answer_schema.dump(answer)}, 200
