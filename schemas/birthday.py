from models.birthday import BirthdayModel
from schemas.CamelCaseSchema import CamelCaseSchema


class BirthdaySchema(CamelCaseSchema):
    class Meta:
        model = BirthdayModel
        load_instance = True
        dump_only = (
            "id",
            "created_at",
            "updated_at",
        )
