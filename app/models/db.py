from aiogram import Dispatcher
from aiogram.utils.executor import Executor
from gino import Gino

from app import config

db = Gino()


class BaseModel(db.Model):
    __abstract__ = True


class TimedBaseModel(BaseModel):
    __abstract__ = True

    created_at = db.Column(db.DateTime(True), server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime(True),
        default=db.func.now(),
        onupdate=db.func.now(),
        server_default=db.func.now(),
    )


async def on_startup(dispatcher: Dispatcher):
    await db.set_bind(config.POSTGRES_URI)


async def on_shutdown(dispatcher: Dispatcher):
    bind = db.pop_bind()
    if bind:
        await bind.close()


def setup(runner: Executor):
    runner.on_startup(on_startup)
    runner.on_shutdown(on_shutdown)
