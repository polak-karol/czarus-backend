from flask_restful import Resource
from flask import request

from schemas.birthday import BirthdaySchema
from models.birthday import BirthdayModel

birthday_schema = BirthdaySchema()


class Birthday(Resource):
    @classmethod
    def get(cls):
        birthdays = BirthdayModel.find_birthday_by_date(request.args["guild_id"], request.args["date"])
        if not birthdays:
            return {"message": "Not found"}, 404

        return {"message": birthday_schema.dump(birthdays, many=True)}, 200

    @classmethod
    def get_by_user(cls):
        print('fe')
        birthdays = BirthdayModel.find_birthday_by_user_id(request.args["guild_id"], request.args["user_id"])
        if not birthdays:
            return {"message": "Not found"}, 404

        return {"message": birthday_schema.dump(birthdays, many=True)}, 200

    @classmethod
    def put(cls):
        birthday_json = request.get_json()
        birthday = BirthdayModel.find_birthday_by_user_id(birthday_json["guild_id"], birthday_json["user_id"], birthday_json["date"]).first()

        if birthday:
            return birthday_schema.dump(birthday), 200

        birthday = birthday_schema.load(birthday_json)

        birthday.save_to_db()

        return birthday_schema.dump(birthday), 200
