from db import db
from models.base import BaseModel


class AnswerConfigModel(BaseModel):
    __tablename__ = "answer_configs"

    id = db.Column(db.Integer, primary_key=True)
    answers_handle_channel_id = db.Column(db.String(300), nullable=True)
    guild_id = db.Column(db.String(300), nullable=False, unique=True)

    @classmethod
    def find_answer_config(cls, guild_id: str) -> "AnswerConfigModel":
        return cls.query.filter_by(guild_id=guild_id)

    @classmethod
    def get_all_config(cls) -> "AnswerConfigModel":
        return cls.query
