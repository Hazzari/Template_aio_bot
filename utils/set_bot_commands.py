from aiogram import types
from loguru import logger


async def set_default_commands(dp):
    logger.info("Установка стандартных команд - подсказок... через '/'")
    await dp.bot.set_my_commands([
        types.BotCommand("example_admin", "(admins only) Команда для админа"),
        types.BotCommand("example_user", "Команда для пользователя"),
        types.BotCommand("get_cat", "Получить картинку котика"),
        types.BotCommand("more_cats", "Получить галерею котиков"),
    ])
