from loguru import logger

from loader import dp
from .private_chat import IsPrivate, IsSuperGroup


if __name__ == "filters":
    logger.info('Настраиваем filters')
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(IsSuperGroup)
