from aiogram import types
from loguru import logger


async def set_default_commands(dp):
    logger.info("Установка стандартных команд - подсказок... через '/'")
    await dp.bot.set_my_commands([
        types.BotCommand("channels", "Подписка на каналы"),
        types.BotCommand("create_post", "Отправить пост"),
    ])
