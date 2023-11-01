from db import db
from sqlalchemy.dialects import postgresql
from models.base import BaseModel


class BirthdayConfigModel(BaseModel):
    __tablename__ = "birthday_configs"

    id = db.Column(db.Integer, primary_key=True)
    birthdays_announcement_channel_id = db.Column(db.String(300), nullable=True)
    birthdays_handle_channel_id = db.Column(db.String(300), nullable=True)
    wishes_singular = db.Column(postgresql.ARRAY(db.String), nullable=True)
    wishes_plural = db.Column(postgresql.ARRAY(db.String), nullable=True)
    guild_id = db.Column(db.String(300), nullable=False, unique=True)

    @classmethod
    def find_birthday_config(cls, guild_id: str) -> "BirthdayConfigModel":
        return cls.query.filter_by(guild_id=guild_id)

    @classmethod
    def get_all_config(cls) -> "BirthdayConfigModel":
        return cls.query
