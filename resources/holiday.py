from flask_restful import Resource
from flask import request

from schemas.holiday import HolidaySchema
from models.holiday import HolidayModel

holiday_schema = HolidaySchema()


class Holiday(Resource):
    @classmethod
    def get(cls, guild_id):
        holiday = HolidayModel.find_holiday(guild_id, request.args["date"]).first()

        if not holiday:
            return {"message": "Not found"}, 404

        return {"message": holiday_schema.dump(holiday)}, 200

    @classmethod
    def put(cls, guild_id):
        holiday_json = request.get_json()
        holiday = HolidayModel.find_holiday(guild_id, holiday_json["date"]).first()

        if holiday:
            return holiday_schema.dump(holiday), 200

        holiday = holiday_schema.load(holiday_json)
        holiday.save_to_db()

        return holiday_schema.dump(holiday), 200
