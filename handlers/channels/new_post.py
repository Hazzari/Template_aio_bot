from aiogram import types
from loguru import logger

from loader import dp


@dp.channel_post_handler(content_types=types.ContentTypes.ANY)
async def new_post(message: types.Message):
    logger.info(f'Новое сообщение в канале {message.chat.title}\n:{message.text}')
