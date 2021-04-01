import asyncio

from data import config
from utils.db_api import quick_command
from utils.db_api.db_gino import db


async def test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    print("Добавляю пользователей в базу данных")
    await quick_command.add_user(1, 'OneUser', 'email@da.dsa')
    await quick_command.add_user(2, 'Алекс', 'eas@mail.coo')
    await quick_command.add_user(3, 'John', 'john@mail.com')
    print('Готово')

    users = await quick_command.select_all_users()
    print(f'Получил всех пользователей: {[x.name for x in users]}')

    count_users = await quick_command.count_users()
    print(f'Всего пользователей {count_users}')

    user = await quick_command.select_user(id=3)
    print(f'Получил пользователя : {user}')


