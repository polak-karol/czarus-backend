from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from helpers.DateTimeHelper import DateTimeHelper
from schemas.drawer import DrawerSchema
from models.drawer import DrawerModel

drawer_schema = DrawerSchema()


class Drawer(Resource):
    @classmethod
    @jwt_required()
    def put(cls):
        if not cls.is_request_authorized(guild_id):
            return {"msg": "You aren't authorized"}, 401

        drawer_json = request.get_json()
        drawer = DrawerModel.find_drawer(
            drawer_json["guild_id"], drawer_json["user_id"], drawer_json["draw_type"]
        ).first()

        if drawer:
            if DateTimeHelper.is_date_in_current_week(drawer.updated_at):
                return {
                    "msg": "User already draw in this week.",
                    "last_vote_date": drawer.updated_at.isoformat(),
                }, 400
        else:
            drawer = drawer_schema.load(drawer_json)

        drawer.save_to_db()

        return drawer_schema.dump(drawer), 200
