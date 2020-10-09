from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

from app import config


def reply(buttons) -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
    markup.add(*buttons)
    return markup


def inline() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("example", callback_data="example"))
    markup.add(InlineKeyboardButton("example", callback_data="example"))
    return markup

