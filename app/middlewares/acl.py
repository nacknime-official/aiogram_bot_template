from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from app import config
from app.models.user import User


class ACLMiddleware(BaseMiddleware):
    async def setup_chat(self, data: dict, user: types.User, message: types.Message):
        user_id = user.id

        user = (await User.get_or_create(id=user_id))[0]

        data["user"] = user

    async def on_pre_process_message(self, message: types.Message, data: dict):
        await self.setup_chat(data, message.from_user, message)
