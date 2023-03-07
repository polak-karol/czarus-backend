from ma import ma
from models.answer import AnswerModel


class AnswerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AnswerModel
        load_instance = True
        dump_only = (
            "id",
            "created_at",
            "updated_at",
        )
