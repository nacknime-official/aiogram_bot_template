from aiogram import types
from aiogram.dispatcher import FSMContext

from app import config, services
from app.misc import dp
from app.models.user import User
from app.utils import markups
from app.utils.states import UserStates


@dp.message_handler(text="Главное меню", state="*")
@dp.message_handler(commands="start", state="*")
async def cmd_start(message: types.Message, user: User, state: FSMContext):
    await message.answer("example")
