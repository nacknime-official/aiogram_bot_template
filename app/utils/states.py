from aiogram.dispatcher.filters.state import State, StatesGroup

from app import config


class UserStates(StatesGroup):
    State = State()


class AdminStates(StatesGroup):
    State = State()
