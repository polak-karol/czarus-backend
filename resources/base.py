import re
import os
import inflection
from flask_restful import Resource
from flask import request
from flask_jwt_extended import get_jwt_identity


class BaseResource(Resource):
    not_authorized_response = {"message": "You are not authorized"}, 401

    @classmethod
    def to_snake(cls, string: str):
        return re.sub("([A-Z]\w+$)", "_\\1", string).lower()

    @classmethod
    def is_client_authorized(cls):
        return get_jwt_identity() or request.headers.get(
            "Bot-Authorization"
        ) == os.getenv("BOT_AUTHORIZATION_TOKEN")

    @classmethod
    def recursive_camelize(cls, data: any):
        if isinstance(data, dict):
            return {inflection.camelize(key, False): cls.recursive_camelize(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [cls.recursive_camelize(item) for item in data]
        else:
            return data

    @classmethod
    def recursive_snake_case(cls, data: any):
        if isinstance(data, dict):
            return {cls.__snake_case(key): cls.recursive_snake_case(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [cls.recursive_snake_case(item) for item in data]
        else:
            return data

    @classmethod
    def __snake_case(cls, string: str):
        return ''.join(['_' + i.lower() if i.isupper() else i for i in string]).lstrip('_')

