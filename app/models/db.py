from aiogram import Dispatcher
from aiogram.utils.executor import Executor
from tortoise import Tortoise, fields
from tortoise.models import Model

from app import config

db = Tortoise()


class BaseModel(Model):
    class Meta:
        abstract = True


class TimedBaseModel(BaseModel):
    class Meta:
        abstract = True

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


async def on_startup(dispatcher: Dispatcher):
    await db.init(config=config.TORTOISE_ORM)


async def on_shutdown(dispatcher: Dispatcher):
    await db.close_connections()


def setup(runner: Executor):
    runner.on_startup(on_startup)
    runner.on_shutdown(on_shutdown)
