import asyncio
import datetime
import re
from pprint import pprint

from aiogram import types
from aiogram.dispatcher.filters import Command, AdminFilter
from aiogram.utils.exceptions import BadRequest, CantRestrictChatOwner, CantRestrictSelf, UserIsAnAdministratorOfTheChat
from loguru import logger

from filters import IsGroup
from loader import bot, dp


@dp.message_handler(IsGroup(), AdminFilter(), regexp=r"(!ro|/ro) ?(\d+)? ?([\w+\D]+)?", is_reply=True)
async def read_only_mode(message: types.Message):
    """
    Хендлер с фильтром в группе, где можно использовать команду !ro ИЛИ /ro, только для администраторов.

    :time int: время на которое нужно замутить пользователя в минутах.
    :reason str: причина мута. При отсутствии времени и/или причины, то
                 используются стандартные значения: 5 минут и None
                 для времени и причины соответственно.
     """
    member = message.reply_to_message.from_user
    chat_id = message.chat.id
    command_parse = re.compile(r'(!ro|/ro) ?(\d+)? ?([\w+\D]+)?')
    parsed = command_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)

    if not time:
        time = 5
    else:
        time = int(time)

    until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)

    ReadOnlyPermissions = types.ChatPermissions(
            can_send_messages=False,
            can_send_media_messages=False,
            can_send_polls=False,
            can_send_other_messages=False,
            can_add_web_page_previews=False,
            can_invite_users=True,
            can_change_info=False,
            can_pin_messages=False,
    )

    try:
        await bot.restrict_chat_member(chat_id,
                                       user_id=member.id,
                                       permissions=ReadOnlyPermissions,
                                       until_date=until_date)
        answer_text_ro = f'Пользователю {member.get_mention(as_html=True)} запрещено писать {time} мин. '
        if comment:
            answer_text_ro += f'По причине {comment}'

        ban_text = await message.answer(answer_text_ro)
        logger.info(answer_text_ro)
        await message.delete()
        # await message.reply_to_message.delete() # если нужно удалить сообщение за которое был забанен
        await asyncio.sleep(time * 60 if time else 5)
        await ban_text.delete()

    except (CantRestrictChatOwner, CantRestrictSelf, UserIsAnAdministratorOfTheChat):
        err_message = await message.answer(f'Пользователь {member.get_mention(as_html=True)} является администратором.')
        await asyncio.sleep(2)
        await err_message.delete()


@dp.message_handler(IsGroup(), AdminFilter(), Command("unro", prefixes='!/'), is_reply=True)
async def undo_read_only_mode(message: types.Message):
    user_allowed = types.ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_polls=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True,
            can_invite_users=True,
            can_change_info=False,
            can_pin_messages=False,
    )
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id

    try:
        await message.chat.restrict(user_id=member_id, permissions=user_allowed, until_date=0)
        await message.reply(f'Пользователь {message.reply_to_message.from_user.full_name} был разбанен')
    except (CantRestrictChatOwner, CantRestrictSelf) as err:
        logger.info(err)


@dp.message_handler(IsGroup(), AdminFilter(), Command('ban', prefixes='!/'), is_reply=True)
async def ban_user(message: types.Message):
    member = message.reply_to_message.from_user
    await message.chat.kick(user_id=ban_user.id)
    await message.reply(f'Пользователь {member.full_name} был забанен')


@dp.message_handler(IsGroup(), AdminFilter(), Command('unban', prefixes='!/'), is_reply=True)
async def unban_user(message: types.Message):
    member = message.reply_to_message.from_user
    await message.chat.unban(user_id=unban_user.id)
    await message.reply(f'Пользователь {member.full_name} был разбанен')
