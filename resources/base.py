import re
import os
from flask_restful import Resource
from flask import request
from flask_jwt_extended import get_jwt_identity


class BaseResource(Resource):
    not_authorized_response = {'message': 'You are not authorized'}, 401

    @classmethod
    def to_snake(cls, string):
        return re.sub("([A-Z]\w+$)", "_\\1", string).lower()

    @classmethod
    def t_dict(cls, value):
        if isinstance(value, list):
            return [cls.t_dict(i) if isinstance(i, (dict, list)) else i for i in value]
        return {
            cls.to_snake(a): cls.t_dict(b) if isinstance(b, (dict, list)) else b
            for a, b in value.items()
        }

    @classmethod
    def is_client_authorized(cls):
        return get_jwt_identity() or request.headers.get('Bot-Authorization') == os.getenv("BOT_AUTHORIZATION_TOKEN")

