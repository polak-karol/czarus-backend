from ma import ma
from models.holiday import HolidayModel


class HolidaySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = HolidayModel
        load_instance = True
        dump_only = (
            "id",
            "created_at",
            "updated_at",
        )
