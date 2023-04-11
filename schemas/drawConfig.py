from schemas.CamelCaseSchema import CamelCaseSchema
from models.drawConfig import DrawConfigModel


class DrawConfigSchema(CamelCaseSchema):
    class Meta:
        model = DrawConfigModel
        load_instance = True
        dump_only = (
            "id",
            "created_at",
            "updated_at",
        )
