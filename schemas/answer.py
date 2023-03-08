from schemas.CamelCaseSchema import CamelCaseSchema
from models.answer import AnswerModel


class AnswerSchema(CamelCaseSchema):
    class Meta:
        model = AnswerModel
        load_instance = True
        dump_only = (
            "id",
            "created_at",
            "updated_at",
        )
