import requests
from flask_jwt_extended import jwt_required

from resources.base import BaseResource


class GuildChannels(BaseResource):
    @classmethod
    @jwt_required()
    def get(cls, guild_id):
        if not cls.is_request_authorized(guild_id):
            return {"msg": "You aren't authorized"}, 401

        reg = requests.get(
            f"https://discordapp.com/api/guilds/{guild_id}/channels",
            headers={
                "Authorization": f"Bot OTkzNTc4MTAzNTM4NDU4NjY0.GBv2ys.H5NzLB_xlkehm31XI4XsrZHhsCeOPGrrKlGvQQ"
            },
        )
        guild_channels = reg.json()

        return {"data": guild_channels}, 200
