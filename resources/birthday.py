from flask import request
from flask_jwt_extended import jwt_required

from resources.base import BaseResource
from schemas.birthday import BirthdaySchema
from models.birthday import BirthdayModel

birthday_schema = BirthdaySchema()


class Birthday(BaseResource):
    @classmethod
    @jwt_required(optional=True)
    def get(cls, guild_id: str):
        if not cls.is_client_authorized():
            return cls.not_authorized_response

        birthday = BirthdayModel.find_birthday_by_user_id(
            guild_id, request.args["user_id"]
        ).first()

        if not birthday:
            return {"msg": "Not found"}, 404

        return {"data": birthday_schema.dump(birthday)}, 200

    @classmethod
    @jwt_required(optional=True)
    def put(cls, guild_id: str):
        if not cls.is_client_authorized():
            return cls.not_authorized_response

        birthday_json = request.get_json()
        birthday_json["guildId"] = guild_id
        birthday_query = BirthdayModel.find_birthday_by_user_id(
            guild_id, birthday_json["userId"]
        )
        birthday = birthday_query.first()

        if birthday:
            birthday_query.update(cls.recursive_snake_case(birthday_json))
        else:
            birthday = birthday_schema.load(birthday_json)

        birthday.save_to_db()

        return {"data": birthday_schema.dump(birthday)}, 200

    @classmethod
    @jwt_required(optional=True)
    def delete(cls, guild_id: str):
        if not cls.is_client_authorized():
            return cls.not_authorized_response

        birthday = BirthdayModel.find_birthday_by_user_id(
            guild_id, request.args["user_id"]
        ).first()

        if not birthday:
            return {"msg": "Item not found"}, 404

        birthday.delete_from_db()

        return {"msg": "Item deleted"}, 200


class BirthdayList(BaseResource):
    @classmethod
    @jwt_required(optional=True)
    def get(cls, guild_id: str):
        if not cls.is_client_authorized():
            return cls.not_authorized_response

        if "date" in request.args:
            birthdays = BirthdayModel.find_birthday_by_date(
                guild_id, request.args["date"]
            )
        else:
            birthdays = BirthdayModel.find_birthday_by_guild_id(guild_id)

        if not birthdays:
            return {"msg": "Not found"}, 404

        return {"data": birthday_schema.dump(birthdays, many=True)}, 200
