
from loguru import logger

from loader import dp
from .throttling import ThrottlingMiddleware
from .database import GetDatabase


if __name__ == "middlewares":
    logger.info('Настраиваем middlewares')
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(GetDatabase())
