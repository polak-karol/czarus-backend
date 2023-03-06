from flask_restful import Resource
from flask import request

from helpers.global_functions import is_date_in_current_week
from schemas.drawer import DrawerSchema
from models.drawer import DrawerModel

drawer_schema = DrawerSchema()


class Drawer(Resource):
    @classmethod
    def get(cls, user_id, guild_id, draw_type):
        drawer = DrawerModel.find_drawer(guild_id, user_id, draw_type).first()
        if not drawer:
            return {"message": "Not found"}, 404

        return {"message": drawer}, 200

    @classmethod
    def put(cls):
        drawer_json = request.get_json()
        drawer = DrawerModel.find_drawer(
            drawer_json["guild_id"], drawer_json["user_id"], drawer_json["draw_type"]
        ).first()

        if drawer:
            if is_date_in_current_week(drawer.updated_at):
                return {"message": "User already draw in this week.", "last_vote_date": drawer.updated_at.isoformat()}, 400
        else:
            drawer = drawer_schema.load(drawer_json)

        drawer.save_to_db()

        return drawer_schema.dump(drawer), 200
