from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hbold, hitalic

from filters import IsPrivate
from loader import dp

from data.config import ADMINS


@dp.message_handler(IsPrivate(), text="secret", user_id=ADMINS)
async def admin_chat_secret(message: types.Message):
    """Хендлер на команду слово secret. Только если админ"""
    await message.answer('Это секретное сообщение, вызванное одним из администраторов в личной переписке')


@dp.message_handler(IsPrivate(), Command("custom", prefixes="/"))
async def start(message: types.Message):
    """Хендлер на команду /custom."""
    content = 'Тут просто какой то текст'
    await message.answer(f"Привет {hbold(message.from_user.full_name)}\n\n"
                         f"Я простой чат-менеджер. !{hitalic(content)}! "
                         f"который пишется в чат. ")
