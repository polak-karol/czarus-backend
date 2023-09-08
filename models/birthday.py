from db import db
from sqlalchemy import text
from datetime import date as date_helper
from models.base import BaseModel


class BirthdayModel(BaseModel):
    __tablename__ = "birthdays"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.String(300), nullable=False)
    guild_id = db.Column(db.String(300), nullable=False)
    is_anonymous = db.Column(db.Boolean, default=False)

    @classmethod
    def find_birthday_by_guild_id(cls, guild_id: str) -> "BirthdayModel":
        return cls.query.filter_by(guild_id=guild_id)

    @classmethod
    def find_birthday_by_user_id(cls, guild_id: str, user_id: str) -> "BirthdayModel":
        return cls.query.filter_by(guild_id=guild_id, user_id=user_id)

    @classmethod
    def find_birthday_by_date(cls, guild_id: str, date) -> "BirthdayModel":
        date_iso_format = date_helper.fromisoformat(date)

        return cls.query.from_statement(
            text(
                f"""
            SELECT
                *
            FROM
                birthdays
            WHERE
                guild_id = {guild_id}::VARCHAR
            AND
                EXTRACT(month FROM date)::INTEGER = {str(date_iso_format.month)}
            AND
                EXTRACT(day FROM date)::INTEGER = {str(date_iso_format.day)};"""
            )
        ).all()
