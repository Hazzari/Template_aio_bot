
from aiogram import Dispatcher
from loguru import logger

from loader import dp
from .throttling import ThrottlingMiddleware


if __name__ == "middlewares":
    logger.info('Настраиваем middlewares')
    dp.middleware.setup(ThrottlingMiddleware())
