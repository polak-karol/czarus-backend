from schemas.camel_case_schema import CamelCaseSchema
from models.draw_config import DrawConfigModel


class DrawConfigSchema(CamelCaseSchema):
    class Meta:
        model = DrawConfigModel
        load_instance = True
        dump_only = (
            "id",
            "created_at",
            "updated_at",
        )
