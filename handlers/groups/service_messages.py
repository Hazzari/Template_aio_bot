from aiogram import types
from aiogram.dispatcher import FSMContext
from loguru import logger

from filters import IsGroup
from loader import dp, bot


@dp.message_handler(IsGroup(), content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def new_member(message: types.Message):
    logger.info(f'Пользователь {message.new_chat_members[0]} зашел в чат.')
    await message.answer(f"Привет, {message.new_chat_members[0]}.")


@dp.message_handler(IsGroup(), content_types=types.ContentTypes.LEFT_CHAT_MEMBER)
async def baned_member(message: types.Message):
    if message.left_chat_member.id == message.from_user.id:
        await message.answer(f'{message.left_chat_member.get_mention(as_html=True)} вышел из чата.')
    elif message.from_user.id == (await bot.me).id:
        return
    else:
        await message.answer(f'{message.left_chat_member.full_name} был удален из чата '
                             f'пользователем {message.from_user.get_mention(as_html=True)}')
