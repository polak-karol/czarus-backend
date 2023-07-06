from db import db
from models.base import BaseModel


class GuildSettingsModel(BaseModel):
    __tablename__ = "guild_settings"

    id = db.Column(db.Integer, primary_key=True)
    birthdays_channel_id = db.Column(db.String(300), nullable=True)
    answers_channel_id = db.Column(db.String(300), nullable=True)
    holiday_channel_id = db.Column(db.String(300), nullable=True)
    guild_id = db.Column(db.String(300), nullable=False, unique=True)

    @classmethod
    def find_guild_settings(cls, guild_id):
        return cls.query.filter_by(guild_id)
