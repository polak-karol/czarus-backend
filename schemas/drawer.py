from marshmallow_enum import EnumField

from schemas.camel_case_schema import CamelCaseSchema
from models.drawer import DrawerModel
from helpers.EnumDrawerType import EnumDrawerType


class DrawerSchema(CamelCaseSchema):
    draw_type = EnumField(EnumDrawerType)

    class Meta:
        model = DrawerModel
        load_instance = True
        dump_only = (
            "id",
            "created_at",
            "updated_at",
        )
