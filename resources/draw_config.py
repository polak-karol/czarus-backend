from flask import request
from flask_jwt_extended import jwt_required

from resources.base import BaseResource
from schemas.draw_config import DrawConfigSchema
from models.draw_config import DrawConfigModel

draw_config_schema = DrawConfigSchema()


class DrawConfig(BaseResource):
    @classmethod
    @jwt_required(optional=True)
    def get(cls, guild_id):
        if not cls.is_client_authorized():
            return cls.not_authorized_response

        draw_config = DrawConfigModel.find_draw_config_by_guild_id(guild_id).first()

        if not draw_config:
            return {"msg": "Not found"}, 404

        return {"data": draw_config_schema.dump(draw_config)}, 200

    @classmethod
    @jwt_required(optional=True)
    def put(cls, guild_id):
        if not cls.is_client_authorized():
            return cls.not_authorized_response

        draw_config_json = request.get_json()
        draw_config_json["guildId"] = guild_id
        draw_config_query = DrawConfigModel.find_draw_config_by_guild_id(guild_id)
        draw_config = draw_config_query.first()

        if draw_config:
            draw_config_query.update(draw_config_schema.load(draw_config_json))
        else:
            draw_config = draw_config_schema.load(draw_config_json)

        draw_config.save_to_db()

        return {"data": draw_config_schema.dump(draw_config)}, 200
