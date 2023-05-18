from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required

from resources.base import BaseResource
from schemas.answer import AnswerSchema
from models.answer import AnswerModel

answer_schema = AnswerSchema()


class Answer(BaseResource):
    @classmethod
    @jwt_required()
    def get(cls, guild_id):
        answer = AnswerModel.find_answer(guild_id).first()

        if not answer:
            return {"message": "Not found"}, 404

        return {"data": answer_schema.dump(answer)}, 200

    @classmethod
    @jwt_required()
    def put(cls, guild_id):
        answer_json = request.get_json()
        answer_query = AnswerModel.find_answer(guild_id)
        answer = answer_query.first()

        if not answer:
            answer = answer_schema.load(answer_json)
        else:
            answer_query.update(cls.t_dict(answer_json))

        answer.save_to_db()

        return {"data": answer_schema.dump(answer)}, 200


class AnswerList(BaseResource):
    @classmethod
    @jwt_required()
    def get(cls, guild_id):
        answer = AnswerModel.find_answer(guild_id).first()

        if not answer:
            return {"message": "Not found"}, 404

        return {"data": answer_schema.dump(answer)}, 200
