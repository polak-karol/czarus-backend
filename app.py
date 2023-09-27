from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import (
    JWTManager,
    get_jwt,
    create_access_token,
    get_jwt_identity,
    set_access_cookies,
)
from flask_migrate import Migrate
from dotenv import load_dotenv
from marshmallow import ValidationError
from datetime import datetime, timezone, timedelta

from db import db
from ma import ma
from blocklist import BLOCKLIST
from resources.drawer import Drawer
from resources.holiday import Holiday, HolidayList
from resources.birthday import Birthday, BirthdayList
from resources.answer import Answer, AnswerList
from resources.draw_config import DrawConfig
from resources.discord_login import DiscordLogin
from resources.user import User
from resources.client_authorization import ClientAuthorization
from resources.discord import DiscordGuildChannels
from resources.guild_settings import GuildSettings, GuildSettingsList

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
load_dotenv(".env", verbose=True)
app.config.from_object("default_config")
app.config.from_envvar("APPLICATION_SETTINGS")
api = Api(app)
jwt = JWTManager(app)
db.init_app(app)
migrate = Migrate(app, db)


@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(days=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        return response


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(error):
    return jsonify(error.messages), 400


@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    return jwt_payload["jti"] in BLOCKLIST


api.add_resource(Drawer, "/drawer/<string:guild_id>")
api.add_resource(Holiday, "/holiday/<string:guild_id>")
api.add_resource(HolidayList, "/holiday/list/<string:guild_id>")
api.add_resource(Birthday, "/birthday/<string:guild_id>")
api.add_resource(BirthdayList, "/birthday/list/<string:guild_id>")
api.add_resource(Answer, "/answer/<string:guild_id>")
api.add_resource(AnswerList, "/answer/list/<string:guild_id>")
api.add_resource(DrawConfig, "/draw-config/<string:guild_id>")
api.add_resource(DiscordLogin, "/discord-login")
api.add_resource(User, "/user")
api.add_resource(ClientAuthorization, "/client-authorization")
api.add_resource(DiscordGuildChannels, "/guild-channels/<string:guild_id>")
api.add_resource(GuildSettings, "/guild-settings/<string:guild_id>")
api.add_resource(GuildSettingsList, "/guild-settings/list")


if __name__ == "__main__":
    ma.init_app(app)
    app.run(host="0.0.0.0", port=5001)
