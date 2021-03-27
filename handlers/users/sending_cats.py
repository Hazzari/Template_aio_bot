from aiogram.dispatcher.filters import Command
from aiogram.types import Message, ContentType, InputFile, MediaGroup

from loader import dp, bot


@dp.message_handler(content_types=ContentType.PHOTO)
async def get_file_id_photo(message: Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=ContentType.VIDEO)
async def get_file_id_video(message: Message):
    await message.reply(message.video.file_id)


@dp.message_handler(Command('get_cat'))
async def send_cat(message: Message):
    photo_file_id = '..'
    photo_url = 'https://proprikol.ru/wp-content/uploads/2020/08/krasivye-kartinki-kotikov-60.jpg'  # 'url://.jpg|png|'
    # photo_bytes = InputFile(path_or_bytesio='photos/cats.jpg')
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo_url,
                         caption='Тут больше фото! /more_cats')

    await message.answer_video('BAACAgIAAxkBAAIEq2BfqjhUUr2ATU0PeVV1tLhpgvjNAALsDQACN3z5SjuCpqSuhtYHHgQ')


@dp.message_handler(Command('more_cats'))
async def more_cats(message: Message):
    cats = [
        'https://i.pinimg.com/originals/f5/24/96/f524965222bdeeb53dc8b6caa2a13c54.jpg',
        'https://www.zastavki.com/pictures/1680x1050/2018Animals___Cats_Large_gray_cat_with_a_surprised_look_123712_16.jpg',
        'https://bipbap.ru/wp-content/uploads/2018/03/PhDXRCLsqz4.jpg',
        'https://cs.pikabu.ru/post_img/big/2013/11/25/5/1385362124_897680212.jpg',
    ]

    album = MediaGroup()
    # photo_file_id = '..'
    photo_url = 'https://proprikol.ru/wp-content/uploads/2020/08/krasivye-kartinki-kotikov-60.jpg'  # 'url://.jpg|png|'
    # photo_bytes = InputFile(path_or_bytesio='photos/cats.jpg')
    # video_file_id = ""
    # album.attach_photo(photo_file_id)
    album.attach_photo(photo_url)
    for cat in cats:
        album.attach_photo(cat)
    # album.attach_photo(photo_bytes)
    # album.attach_photo(video_file_id,
    #                    caption='Видео смешного котика')
    # await bot.send_media_group(chat_id=message.from_user.id, media=album)
    await message.answer_media_group(media=album)
