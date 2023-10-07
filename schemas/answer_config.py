from schemas.camel_case_schema import CamelCaseSchema
from models.answer_config import AnswerConfigModel


class AnswerConfigSchema(CamelCaseSchema):
    class Meta:
        model = AnswerConfigModel
        load_instance = True
        dump_only = (
            "created_at",
            "updated_at",
        )
