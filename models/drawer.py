from db import db
from models.base import BaseModel
from helpers.EnumDrawerType import DrawerType


class DrawerModel(BaseModel):
    __tablename__ = "drawers"

    id = db.Column(db.Integer, primary_key=True)
    draw_type = db.Column(db.Enum(DrawerType), nullable=False)
    user_id = db.Column(db.String(300), nullable=False)
    guild_id = db.Column(db.String(300), nullable=False)

    @classmethod
    def find_drawer(cls, guild_id, user_id, draw_type):
        return cls.query.filter_by(guild_id=guild_id, user_id=user_id, draw_type=draw_type)
