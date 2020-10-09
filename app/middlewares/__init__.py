from aiogram import Dispatcher

from app.middlewares.acl import ACLMiddleware
from app.middlewares.throttling import ThrottlingMiddleware


def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware(limit=0.7))
    dp.middleware.setup(ACLMiddleware())
