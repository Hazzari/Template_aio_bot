from aiogram import Dispatcher
from loguru import logger

from loader import dp

# from .is_admin import AdminFilter
from .forwarded_message import IsForwarded


if __name__ == "filters":
    logger.info('Настраиваем filters')
    dp.filters_factory.bind(IsForwarded)
