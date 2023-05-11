from db import db
from models.base import BaseModel
from sqlalchemy.dialects.postgresql import JSONB


class DrawConfigModel(BaseModel):
    __tablename__ = "draw_configs"

    id = db.Column(db.Integer, primary_key=True)
    guild_id = db.Column(db.String(300), nullable=False)
    writing_config = db.Column(JSONB)
    painting_config = db.Column(JSONB)
    music_config = db.Column(JSONB)

    @classmethod
    def find_draw_config_by_guild_id(cls, guild_id: str) -> "DrawConfigModel":
        return cls.query.filter_by(guild_id=guild_id)
