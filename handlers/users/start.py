import sqlite3
from enum import Enum, auto

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name

    try:
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        print(err)

    count_users = db.count_users()[0][0]

    if count_users == 2 or count_users == 3 or count_users == 4:
        ending = 'еля'
    elif count_users == 1:
        ending = 'ель'

    else:
        ending = 'елей'
    await message.answer(
            "\n".join([
                f'Привет, {message.from_user.full_name}!',
                'Ты был занесен в базу',
                f'В базе <b>{count_users}</b> пользоват{ending}',
            ])
    )
