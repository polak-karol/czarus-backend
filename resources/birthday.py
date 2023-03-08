from flask_restful import Resource
from flask import request

from schemas.birthday import BirthdaySchema
from models.birthday import BirthdayModel

birthday_schema = BirthdaySchema()


class Birthday(Resource):
    @classmethod
    def get(cls, guild_id):
        birthday = BirthdayModel.find_birthday_by_user_id(guild_id, request.args["user_id"]).first()

        if not birthday:
            return {"message": "Not found"}, 404

        return {"message": birthday_schema.dump(birthday)}, 200

    @classmethod
    def put(cls, guild_id):
        birthday_json = request.get_json()
        birthday_json["guild_id"] = guild_id
        birthday = BirthdayModel.find_birthday_by_user_id(guild_id, birthday_json["user_id"]).first()

        if birthday:
            return birthday_schema.dump(birthday), 200

        birthday = birthday_schema.load(birthday_json)
        birthday.save_to_db()

        return birthday_schema.dump(birthday), 200

    @classmethod
    def delete(cls, guild_id):
        birthday = BirthdayModel.find_birthday_by_user_id(guild_id, request.args["user_id"]).first()

        if not birthday:
            return {"message": "Item not found"}, 404

        birthday.delete_from_db()

        return {"message": "Item deleted"}, 200


class BirthdayList(Resource):
    @classmethod
    def get(cls, guild_id):
        if "date" in request.args:
            birthdays = BirthdayModel.find_birthday_by_date(guild_id, request.args["date"])
        else:
            birthdays = BirthdayModel.find_birthday_by_guild_id(guild_id)

        if not birthdays:
            return {"message": "Not found"}, 404

        return {"message": birthday_schema.dump(birthdays, many=True)}, 200
