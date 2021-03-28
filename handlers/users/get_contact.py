from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import contact_buttons
from loader import dp


@dp.message_handler(Command('callback'))
async def share_number(message: types.Message):
    await message.answer(
            f'Здравствуйте, {message.from_user.full_name}.\n'
            f'отправьте нам свой контакт'
            f'нажав на кнопку ниже!',
            reply_markup=contact_buttons.keyboard,
    )


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message: types.Message):
    contact = message.contact
    await message.answer(
            f'Спасибо {contact.full_name}\n'
            f'Ваш номер {contact.phone_number} был получен',
            reply_markup=ReplyKeyboardRemove()
    )
