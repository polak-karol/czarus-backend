from flask_restful import Resource
from flask import request

from schemas.answer import AnswerSchema
from models.answer import AnswerModel

answer_schema = AnswerSchema()


class Answer(Resource):
    @classmethod
    def get(cls, guild_id):
        answer = AnswerModel.find_answer(guild_id).first()

        if not answer:
            return {"message": "Not found"}, 404

        return {"data": answer_schema.dump(answer)}, 200

    @classmethod
    def put(cls, guild_id):
        answer_json = request.get_json()
        answer_query = AnswerModel.find_answer(guild_id)
        answer = answer_query.first()

        if not answer:
            answer = answer_schema.load(answer_json)
        else:
            answer_query.update(answer_json)

        answer.save_to_db()

        return {"data": answer_schema.dump(answer)}, 200


class AnswerList(Resource):
    @classmethod
    def get(cls, guild_id):
        answer = AnswerModel.find_answer(guild_id).first()

        if not answer:
            return {"message": "Not found"}, 404

        return {"data": answer_schema.dump(answer)}, 200
