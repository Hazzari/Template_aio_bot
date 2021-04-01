from aiogram import executor
from loguru import logger

from loader import dp
import middlewares
import filters
import handlers
from utils.db_api import db_gino
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from loader import db
from utils.db_api import db_gino


async def on_startup(dispatcher: dp):
    logger.info('Подключаем БД')
    await db_gino.on_startup(dispatcher)

    logger.info('Чистим БД')
    await db.gino.drop_all()

    logger.info('Создаем таблицы')
    await db.gino.create_all()

    await on_startup_notify(dispatcher)
    await set_default_commands(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
