from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.deep_linking import get_start_link
from re import compile as cpl

from filters import IsPrivate
from loader import dp


PATTERN = r"\w+"


@dp.message_handler(CommandStart(deep_link=cpl(PATTERN), encoded=True), IsPrivate())
async def bot_start_deeplink(message: types.Message):
    """ Ловим сообщение /start + переданный url."""

    deep_link_args = message.get_args()

    await message.answer(f"Привет, {message.from_user.full_name}!\n"
                         f"В вашей команде есть диплинк\n"
                         f"Вы передали аргумент команде start: {deep_link_args}.\n")


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    """Новый вариант передаем в /start + значение."""

    deep_link = await get_start_link('s2qwe', encode=True)

    await message.answer(f"Привет, {message.from_user.full_name}!\n"
                         f"Личная переписка.\n"
                         f"В вашей команде нет диплинка.\n"
                         f"Ваша диплинк ссылка {deep_link}")
