from ma import ma


class CamelCaseSchema(ma.SQLAlchemyAutoSchema):
    """Schema that uses camel-case for its external representation
    and snake-case for its internal representation.
    """

    @classmethod
    def camelcase(cls, s):
        parts = iter(s.split("_"))
        return next(parts) + "".join(i.title() for i in parts)

    @classmethod
    def on_bind_field(cls, field_name, field_obj):
        field_obj.data_key = cls.camelcase(field_obj.data_key or field_name)
