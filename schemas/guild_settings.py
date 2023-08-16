from ma import ma

from models.guild_settings import GuildSettingsModel


class GuildSettingsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GuildSettingsModel
        load_instance = True
        dump_only = (
            "created_at",
            "updated_at",
        )
