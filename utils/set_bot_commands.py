from aiogram import types
from loguru import logger


async def set_default_commands(dp):
    logger.info("Установка стандартных команд - подсказок... через '/'")
    await dp.bot.set_my_commands([
        types.BotCommand("example_admin", "(admins only) Команда для админа"),
        types.BotCommand("example_user", "Команда для пользователя"),
        types.BotCommand("set_photo", "Установить фото в чате"),
        types.BotCommand("set_title", "Установить название группы"),
        types.BotCommand("set_description", "Установить описание группы"),
        types.BotCommand("ro", "Режим Read only"),
        types.BotCommand("unro", "Отключить RO"),
        types.BotCommand("ban", "Забанить"),
        types.BotCommand("unban", "Разбанить"),
    ])
