from aiogram import executor

from loader import dp
import middlewares
import filters
import handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from loader import db


async def on_startup(dispatcher):

    await on_startup_notify(dispatcher)
    await set_default_commands(dispatcher)
    try:
        db.create_table_users()
    except Exception as err:
        print(err)

    # db.delete_users()
    print(db.select_all_users())


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
