from aiogram import Dispatcher
from loguru import logger

from loader import dp

from .is_admin import CustomAdminFilter
from .group_chat import IsGroup


if __name__ == "filters":
    logger.info('Настраиваем filters')
    dp.filters_factory.bind(CustomAdminFilter)
    dp.filters_factory.bind(IsGroup)
