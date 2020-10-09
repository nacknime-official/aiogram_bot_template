from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.utils.executor import Executor

from app import config

bot = Bot(config.TELEGRAM_TOKEN)
storage = RedisStorage2(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=config.REDIS_FSM_DB,
    prefix=config.REDIS_FSM_PREFIX,
)
dp = Dispatcher(bot, storage=storage)
runner = Executor(dp)


def setup():
    from app.models import db
    from app import filters

    db.setup(runner)
    filters.setup(dp)
