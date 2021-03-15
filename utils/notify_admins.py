from aiogram import Dispatcher

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Запущен, работаем с кнопками!")

        except Exception as err:
            from loguru import logger
            logger.exception(err)
