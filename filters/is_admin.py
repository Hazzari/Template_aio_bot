from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class CustomAdminFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        print('Проверка работы фильтра')
        member = await message.chat.get_member(message.from_user.id)
        return member.is_chat_admin()
