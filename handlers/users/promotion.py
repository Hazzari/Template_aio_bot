from aiogram import types
from aiogram.dispatcher.filters.builtin import ForwardedMessageFilter, Command

from data.config import CHANNELS
from filters import IsForwarded
from keyboards.inline.subscription import check_button
from loader import dp, bot

# @dp.message_handler(ForwardedMessageFilter(is_forwarded=True))
from utils.misc import subscription


@dp.message_handler(IsForwarded(), content_types=types.ContentTypes.ANY)
async def get_channel_info(message: types.Message):
    answer_text = f'Сообщение прислано из канала {message.forward_from_chat.title}.\n' \
                  f'Username: @{message.forward_from_chat.username}.\n' \
                  f'ID: {message.forward_from_chat.id}'

    await message.answer(answer_text)


@dp.message_handler(Command("channels"))
async def show_channels(messame: types.Message):
    channels_format = str()
    for channel_id_or_username in CHANNELS:
        chat = await bot.get_chat(channel_id_or_username)
        invite_link = await chat.export_invite_link()
        channels_format += f'Канал <a href="{invite_link}">{chat.title}</a>\n\n'

    await messame.answer(f'Список каналов для подписки:\n'
                         f'{channels_format}',
                         reply_markup=check_button,
                         disable_web_page_preview=True)


@dp.callback_query_handler(text='check_subs')
async def checker(call: types.CallbackQuery):
    await call.answer()  # убираем часики
    await call.message.edit_reply_markup()  # Убираем клавиатуру
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id, channel=channel)

        channel = await bot.get_chat(channel)

        if status:
            result += f'Подписка на канал <b>{channel.title}</b> оформлена!\n\n'
        else:
            invite_link = await channel.export_invite_link()
            result += f'Подписка на канал <b>{channel.title}</b> НЕ оформлена!\n' \
                      f'Нужно подписаться на <a href="{invite_link}">канал</a>\n\n '

    await call.message.answer(result, disable_web_page_preview=True)
