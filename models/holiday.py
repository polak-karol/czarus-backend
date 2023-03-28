from datetime import datetime

from db import db
from models.base import BaseModel


class HolidayModel(BaseModel):
    __tablename__ = "holidays"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)
    guild_id = db.Column(db.String(300), nullable=False)

    @classmethod
    def find_holiday(cls, guild_id: str, date: str) -> "HolidayModel":
        return cls.query.filter(cls.guild_id == guild_id, cls.date == date)

    @classmethod
    def find_holidays_in_range(cls, guild_id: str, dates):
        return cls.query.filter(cls.guild_id == guild_id, cls.date.between(dates["startDate"], dates["endDate"]))
