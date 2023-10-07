from schemas.camel_case_schema import CamelCaseSchema
from models.birthday_config import BirthdayConfigModel


class BirthdayConfigSchema(CamelCaseSchema):
    class Meta:
        model = BirthdayConfigModel
        load_instance = True
        dump_only = (
            "created_at",
            "updated_at",
        )
