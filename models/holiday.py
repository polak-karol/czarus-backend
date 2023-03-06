from db import db
from models.base import BaseModel


class HolidayModel(BaseModel):
    __tablename__ = "holidays"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    guild_id = db.Column(db.String(300), nullable=False)

    @classmethod
    def find_holiday(cls, guild_id: str, date: str) -> "HolidayModel":
        return cls.query.filter_by(guild_id=guild_id, date=date)
