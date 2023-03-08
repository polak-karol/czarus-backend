from schemas.CamelCaseSchema import CamelCaseSchema
from models.holiday import HolidayModel


class HolidaySchema(CamelCaseSchema):
    class Meta:
        model = HolidayModel
        load_instance = True
        dump_only = (
            "id",
            "created_at",
            "updated_at",
        )
