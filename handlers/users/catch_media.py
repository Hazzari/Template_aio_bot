from aiogram import types
from loguru import logger

from loader import dp


@dp.message_handler()
async def catch_message(message: types.Message):
    logger.info(message.text)
    await message.answer(f'вы передали {message.text}')


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def catch_document(message: types.Message):
    await message.document.download()
    await message.reply(f' скачан\n'
                        f'<pre>Документ ID = {message.document.file_id}</pre>',
                        parse_mode='HTML')


@dp.message_handler(content_types=types.ContentType.VOICE)
async def catch_voice(message: types.Message):
    await message.voice.download()
    await message.reply(f'Звукозапись скачана\n'
                        f'<pre>Звукозапись ID = {message.voice.file_id}</pre>',
                        parse_mode='HTML')


@dp.message_handler(content_types=types.ContentType.AUDIO)
async def catch_audio(message: types.Message):
    await message.audio.download()
    await message.reply(f'Аудиозапись скачана\n'
                        f'<pre>Аудио ID = {message.audio.file_id}</pre>',
                        parse_mode='HTML')


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def catch_video(message: types.Message):
    await message.video.download()
    await message.reply(f'Видеозапись скачана\n'
                        f'<pre>Видеозапись ID = {message.video.file_id}</pre>',
                        parse_mode='HTML')


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def catch_photo(message: types.Message):
    await message.photo[-1].download()
    await message.reply(f'Фотография скачана\n'
                        f'<pre>Фотография ID = {message.photo[0].file_id}</pre>',
                        parse_mode='HTML')


@dp.message_handler(content_types=types.ContentType.ANY)
async def catch_any(message: types.Message):
    await message.reply(f'Вы прислали\n'
                        f'<pre>any ID = {message.content_type}</pre>',
                        parse_mode='HTML')
