from flask import request
from flask_jwt_extended import jwt_required

from resources.base import BaseResource
from helpers.DateTimeHelper import DateTimeHelper
from schemas.drawer import DrawerSchema
from models.drawer import DrawerModel

drawer_schema = DrawerSchema()


class Drawer(BaseResource):
    @classmethod
    @jwt_required(optional=True)
    def get(cls, guild_id):
        if not cls.is_client_authorized():
            return cls.not_authorized_response
        print(guild_id)
        drawer = DrawerModel.find_drawer(
            guild_id, request.args["user_id"], request.args["draw_type"]
        ).first()

        if drawer:
            return drawer_schema.dump(drawer), 200

        return {'msg': 'Not found.'}, 404

    @classmethod
    @jwt_required(optional=True)
    def put(cls, guild_id):
        if not cls.is_client_authorized():
            return cls.not_authorized_response
        drawer_json = request.get_json()
        drawer_json["guildId"] = guild_id
        drawer_snake = cls.recursive_snake_case(drawer_json)
        drawer_query = DrawerModel.find_drawer(
            drawer_snake["guild_id"], drawer_snake["user_id"], drawer_snake["draw_type"]
        )
        drawer = drawer_query.first()

        if drawer:
            if DateTimeHelper.is_date_in_current_week(drawer.updated_at):
                return {
                    "msg": "User already draw in this week.",
                    "lastVoteDate": drawer.updated_at.isoformat(),
                }, 400
            drawer_query.update(drawer_snake)
        else:
            drawer = drawer_schema.load(drawer_json)

        drawer.save_to_db()

        return drawer_schema.dump(drawer), 200
