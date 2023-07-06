import requests
import os
from flask_jwt_extended import jwt_required

from resources.base import BaseResource


class DiscordGuildChannels(BaseResource):

    @classmethod
    @jwt_required()
    def get(cls, guild_id):
        headers = {"Authorization": f"Bot {os.getenv('DISCORD_APP_BOT_TOKEN')}"}
        response_channels = requests.get(
            f"https://discordapp.com/api/guilds/{guild_id}/channels", headers=headers
        )
        channels = response_channels.json()

        if 'code' in channels:
            return {"message": "Can't fetch data"}, 400

        return {"data": channels}, 200
