from marshmallow_enum import EnumField

from ma import ma
from models.drawer import DrawerModel
from helpers.EnumDrawerType import EnumDrawerType


class DrawerSchema(ma.SQLAlchemyAutoSchema):
    draw_type = EnumField(EnumDrawerType)

    class Meta:
        model = DrawerModel
        load_instance = True
        dump_only = (
            "id",
            "created_at",
            "updated_at",
        )
