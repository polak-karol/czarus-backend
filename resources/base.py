import re
from flask_restful import Resource


class BaseResource(Resource):
    @classmethod
    def to_snake(cls, string):
        return re.sub('([A-Z]\w+$)', '_\\1', string).lower()

    @classmethod
    def t_dict(cls, value):
        if isinstance(value, list):
            return [cls.t_dict(i) if isinstance(i, (dict, list)) else i for i in value]
        return {cls.to_snake(a): cls.t_dict(b) if isinstance(b, (dict, list)) else b for a, b in value.items()}
