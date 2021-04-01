from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from utils.db_api import quick_command as commands


@dp.message_handler(Command('email'))
async def add_email(message: types.Message, state: FSMContext):
    await message.answer("Пришли мне свой email")
    await state.set_state('email')


@dp.message_handler(state='email')
async def enter_email(message: types.Message, state: FSMContext):
    email = message.text
    await commands.update_user_email(email=email, id=message.from_user.id)

    user = await commands.select_user(id=message.from_user.id)
    await message.answer(f'Данные были обновлены. Запись в бд: \n'
                         f'{user.id}\n'
                         f'{user.name}\n'
                         f'{user.email}\n'
                         )
    await state.finish()
