from ma import ma
from models.birthday import BirthdayModel


class BirthdaySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BirthdayModel
        load_instance = True
        dump_only = (
            "id",
            "created_at",
            "updated_at",
        )
