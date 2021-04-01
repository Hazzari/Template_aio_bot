from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from utils.db_api import quick_command as commands


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name

    await commands.add_user(id=message.from_user.id, name=name)

    count_users = await commands.count_users()

    await message.answer(
            "\n".join([
                f'Привет, {message.from_user.full_name}!',
                'Ты был занесен в базу',
                f'Пользователей в базе: <b>{count_users}</b> ',
            ])
    )
