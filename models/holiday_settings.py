from db import db
from models.base import BaseModel


class HolidayConfigsModel(BaseModel):
    __tablename__ = "holiday_configs"

    id = db.Column(db.Integer, primary_key=True)
    holiday_announcement_channel_id = db.Column(db.String(300), nullable=True)
    guild_id = db.Column(db.String(300), nullable=False, unique=True)

    @classmethod
    def find_holiday_config(cls, guild_id):
        return cls.query.filter_by(guild_id=guild_id)

    @classmethod
    def get_all_config(cls):
        return cls.query
