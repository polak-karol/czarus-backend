from flask_jwt_extended import get_jwt_identity, jwt_required

from resources.base import BaseResource
from models.user import UserModel
from schemas.user import UserSchema

user_schema = UserSchema()
dump_user_schema = UserSchema(only=['id', 'username', 'email', 'avatar', 'locale'])


class User(BaseResource):
    @classmethod
    @jwt_required()
    def get(cls):
        user_id = get_jwt_identity()
        user = UserModel.find_by_id(user_id)

        return {"data": {"user": dump_user_schema.dump(user)}}, 200
