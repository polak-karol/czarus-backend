from schemas.camel_case_schema import CamelCaseSchema
from models.user import UserModel


class UserSchema(CamelCaseSchema):
    class Meta:
        model = UserModel
        load_instance = True
        dump_only = (
            "created_at",
            "updated_at",
        )
