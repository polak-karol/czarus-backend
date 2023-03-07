from sqlalchemy.dialects import postgresql

from db import db
from models.base import BaseModel


class AnswerModel(BaseModel):
    __tablename__ = "answers"

    id = db.Column(db.Integer, primary_key=True)
    why_answers = db.Column(postgresql.ARRAY(db.String))
    does_answers = db.Column(postgresql.ARRAY(db.String))
    when_answers = db.Column(postgresql.ARRAY(db.String))
    what_do_you_think_answers = db.Column(postgresql.ARRAY(db.String))
    how_answers = db.Column(postgresql.ARRAY(db.String))
    who_answers = db.Column(postgresql.ARRAY(db.String))
    what_answers = db.Column(postgresql.ARRAY(db.String))
    what_is_answers = db.Column(postgresql.ARRAY(db.String))
    guild_id = db.Column(db.String(300), nullable=False)
    channel_id = db.Column(db.String(300), nullable=False)

    @classmethod
    def find_answer(cls, guild_id: str) -> "AnswerModel":
        return cls.query.filter_by(guild_id=guild_id)
