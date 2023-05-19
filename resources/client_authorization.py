from flask import request
from flask_jwt_extended import create_refresh_token, create_access_token
import os

from resources.base import BaseResource


class ClientAuthorization(BaseResource):

    @classmethod
    def post(cls):
        client_authorization_json = request.get_json()

        if 'token' not in client_authorization_json or client_authorization_json['token'] != os.getenv("SUPER_TOKEN"):
            error_response = {
                "error": request.args["error"],
                "error_description": request.args["error_description"],
            }
            return error_response

        access_token = create_access_token(identity=client_authorization_json['token'], fresh=True, expires_delta=False)
        refresh_token = create_refresh_token(client_authorization_json['token'])

        return {
            "data": {
                "accessToken": access_token,
                "refreshToken": refresh_token
            }
        }, 200
