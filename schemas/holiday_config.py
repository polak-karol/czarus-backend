from schemas.camel_case_schema import CamelCaseSchema
from models.holiday_config import HolidayConfigModel


class HolidayConfigSchema(CamelCaseSchema):
    class Meta:
        model = HolidayConfigModel
        load_instance = True
        dump_only = (
            "created_at",
            "updated_at",
        )
