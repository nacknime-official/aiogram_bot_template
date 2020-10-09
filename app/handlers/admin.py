from aiogram import types
from aiogram.dispatcher import FSMContext

from app import config, services
from app.misc import bot, dp
from app.models.user import User
from app.utils import helper, markups
from app.utils.states import AdminStates


@dp.message_handler(commands="example", is_admin=True, state="*")
async def cmd_example(message: types.Message, state: FSMContext):
    await message.answer("example")
