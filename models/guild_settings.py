from db import db
from models.base import BaseModel


class GuildSettingsModel(BaseModel):
    __tablename__ = "guild_settings"

    id = db.Column(db.Integer, primary_key=True)
    guild_id = db.Column(db.String(300), nullable=False, unique=True)
    language = db.Column(db.String(2), nullable=True)
    timezone = db.Column(db.String(50), nullable=True)

    @classmethod
    def find_guild_settings(cls, guild_id: str) -> "GuildSettingsModel":
        return cls.query.filter_by(guild_id=guild_id)

    @classmethod
    def get_all_settings(cls) -> "GuildSettingsModel":
        return cls.query
