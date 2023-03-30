from flask import request

from resources.base import BaseResource
from schemas.drawConfig import DrawConfigSchema
from models.drawConfig import DrawConfigModel

draw_config_schema = DrawConfigSchema()


class DrawConfig(BaseResource):
    @classmethod
    def get(cls, guild_id):
        draw_config = DrawConfigModel.find_birthday_by_user_id(
            guild_id, request.args["user_id"]
        ).first()

        if not draw_config:
            return {"message": "Not found"}, 404

        return {"data": draw_config_schema.dump(draw_config)}, 200


