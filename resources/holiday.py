from flask import request
from flask_jwt_extended import jwt_required
from datetime import datetime

from resources.base import BaseResource
from schemas.holiday import HolidaySchema
from models.holiday import HolidayModel

holiday_schema = HolidaySchema()


class Holiday(BaseResource):
    @classmethod
    @jwt_required()
    def get(cls, guild_id):
        if not cls.is_request_authorized(guild_id):
            return {"msg": "You aren't authorized"}, 401

        holiday = HolidayModel.find_holiday(guild_id, request.args["date"]).first()

        if not holiday:
            return {"msg": "Not found"}, 404

        return {"data": holiday_schema.dump(holiday)}, 200

    @classmethod
    @jwt_required()
    def put(cls, guild_id):
        if not cls.is_request_authorized(guild_id):
            return {"msg": "You aren't authorized"}, 401

        holiday_json = request.get_json()
        holiday_json["guildId"] = guild_id
        holiday_json["date"] = datetime.fromisoformat(holiday_json["date"]).strftime(
            "%Y-%m-%d"
        )
        holiday_query = HolidayModel.find_holiday(guild_id, holiday_json["date"])
        holiday = holiday_query.first()

        if holiday:
            holiday_query.update(cls.t_dict(holiday_json))
        else:
            holiday = holiday_schema.load(holiday_json)

        holiday.save_to_db()

        return {"data": holiday_schema.dump(holiday)}, 200


class HolidayList(BaseResource):
    @classmethod
    @jwt_required()
    def get(cls, guild_id):
        if not cls.is_request_authorized(guild_id):
            return {"msg": "You aren't authorized"}, 401

        holidays = HolidayModel.find_holidays_in_range(guild_id, request.args)

        if not holidays:
            return {"msg": "Not found"}, 404

        return {"data": holiday_schema.dump(holidays, many=True)}, 200
