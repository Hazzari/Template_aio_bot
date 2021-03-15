from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp


@dp.message_handler(Command('menu'))
async def show_menu(message: types.Message):
    await message.answer("Выберите товар", reply_markup=menu)


@dp.message_handler(text='Штаны')
async def get_pants(message: types.Message):
    await message.answer('Вы выбрали Штаны.')


# @dp.message_handler(Text(endswith='ки'))
@dp.message_handler(Text(equals=['Кросовки', 'Носки']))
async def name_function(message: types.Message):
    await message.answer(f"Вы выбрали {message.text}", reply_markup=ReplyKeyboardRemove())
