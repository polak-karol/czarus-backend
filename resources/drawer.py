from flask_restful import Resource

from models.drawer import DrawerModel


class Drawer(Resource):
    @classmethod
    def get(cls, user_id, guild_id, draw_type):
        drawer = DrawerModel.find_drawer(guild_id, user_id, draw_type)
        if not drawer:
            return {"message": "Not found"}, 404

        return {"message": "Object found"}, 200
