from schemas.camel_case_schema import CamelCaseSchema
from models.guild_settings import GuildSettingsModel


class GuildSettingsSchema(CamelCaseSchema):
    class Meta:
        model = GuildSettingsModel
        load_instance = True
        dump_only = (
            "created_at",
            "updated_at",
        )
