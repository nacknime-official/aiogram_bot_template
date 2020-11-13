from tortoise import fields

from .db import TimedBaseModel


class User(TimedBaseModel):
    id = fields.IntField(pk=True)

    class Meta:
        table = "users"
