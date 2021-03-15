from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from utils.db_api.user import User
from utils.misc import rate_limit


@rate_limit(limit=10)
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, user: User, url):
    await message.answer(f"message: {message}!")
    await message.answer(f"user: {user}!")
    await message.answer(f"url: {url.pop()}")
