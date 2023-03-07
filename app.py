from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from dotenv import load_dotenv
from marshmallow import ValidationError

from db import db
from ma import ma
from blocklist import BLOCKLIST
from resources.drawer import Drawer
from resources.holiday import Holiday
from resources.birthday import Birthday, BirthdayList
from resources.answer import Answer

app = Flask(__name__)
load_dotenv(".env", verbose=True)
app.config.from_object("default_config")
app.config.from_envvar("APPLICATION_SETTINGS")
api = Api(app)
jwt = JWTManager(app)
db.init_app(app)
migrate = Migrate(app, db)


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(error):
    return jsonify(error.messages), 400


@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    return jwt_payload["jti"] in BLOCKLIST


api.add_resource(Drawer, "/drawer/<string:guild_id>")
api.add_resource(Holiday, "/holiday/<string:guild_id>")
api.add_resource(Birthday, "/birthday/<string:guild_id>")
api.add_resource(BirthdayList, "/birthday/list/<string:guild_id>")
api.add_resource(Answer, "/answer/<string:guild_id>")


if __name__ == "__main__":
    ma.init_app(app)
    app.run(host="0.0.0.0", port=5000)
