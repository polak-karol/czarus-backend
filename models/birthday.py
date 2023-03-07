from db import db
from models.base import BaseModel


class BirthdayModel(BaseModel):
    __tablename__ = "birthdays"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.String(300), nullable=False)
    guild_id = db.Column(db.String(300), nullable=False)
    is_anonymous = db.Column(db.Boolean, default=False)

    @classmethod
    def find_birthday_by_user_id(
        cls, guild_id: str, user_id: str
    ) -> "BirthdayModel":
        return cls.query.filter_by(guild_id=guild_id, user_id=user_id)

    @classmethod
    def find_birthday_by_date(cls, guild_id: str, date) -> "BirthdayModel":
        return cls.query.filter_by(guild_id=guild_id, date=date)
