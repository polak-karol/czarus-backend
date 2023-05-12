from db import db
from models.base import BaseModel


class UserModel(BaseModel):
    __tablename__ = "users"

    id = db.Column(db.String(256), primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    global_name = db.Column(db.String(64))
    display_name = db.Column(db.String(64))
    avatar = db.Column(db.String(128))
    discriminator = db.Column(db.String(4))
    public_flags = db.Column(db.Integer)
    flags = db.Column(db.Integer)
    banner = db.Column(db.String(128))
    banner_color = db.Column(db.String(7))
    accent_color = db.Column(db.Integer)
    locale = db.Column(db.String(2))
    mfa_enabled = db.Column(db.Boolean)
    premium_type = db.Column(db.Integer)
    avatar_decoration = db.Column(db.String(128))
    discord_access_token = db.Column(db.String(128))
    verified = db.Column(db.Boolean)

    @classmethod
    def find_by_id(cls, user_id: str) -> "UserModel":
        return cls.query.filter_by(id=user_id)
