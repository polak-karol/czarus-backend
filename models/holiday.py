from sqlalchemy import text
from datetime import date

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
        start_date = date.fromisoformat(dates["startDate"])
        end_date = date.fromisoformat(dates["endDate"])

        return cls.query.from_statement(
            text(
                f"""
            SELECT 
                * 
            FROM 
                holidays 
            WHERE 
                date 
            BETWEEN 
                make_date(EXTRACT(year FROM date)::INTEGER, {str(start_date.month)}, {str(start_date.day)}) 
            AND 
                make_date(EXTRACT(year FROM date)::INTEGER, {str(end_date.month)}, {str(end_date.day)}) 
            AND 
                guild_id = {guild_id};"""
            )
        ).all()
