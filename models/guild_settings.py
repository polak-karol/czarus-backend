from db import db
from models.base import BaseModel


class GuildSettingsModel(BaseModel):
    __tablename__ = "guild_settings"

    id = db.Column(db.Integer, primary_key=True)
    birthdays_announcement_channel_id = db.Column(db.String(300), nullable=True)
    birthdays_handle_channel_id = db.Column(db.String(300), nullable=True)
    answers_channel_id = db.Column(db.String(300), nullable=True)
    holiday_announcement_channel_id = db.Column(db.String(300), nullable=True)
    draw_challenges_writing_handle_channel_id = db.Column(db.String(300), nullable=True)
    draw_challenges_graphic_handle_channel_id = db.Column(db.String(300), nullable=True)
    draw_challenges_music_handle_channel_id = db.Column(db.String(300), nullable=True)
    guild_id = db.Column(db.String(300), nullable=False, unique=True)

    @classmethod
    def find_guild_settings(cls, guild_id):
        return cls.query.filter_by(guild_id=guild_id)

    @classmethod
    def get_all_settings(cls):
        return cls.query
