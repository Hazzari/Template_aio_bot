# имитация пользователя из базы данных
from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from utils.db_api.user import User


class GetDatabase(BaseMiddleware):

    async def on_process_message(self, message: types.Message, data: dict) -> None:
        data["user"] = User(_id=66, name=message.from_user.full_name)
        data["url"] = {message.from_user.url}

    async def on_process_callback_query(self, cq: types.CallbackQuery, data: dict) -> None:
        data["user"] = User(_id=66, name=cq.from_user.full_name)
