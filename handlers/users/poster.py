from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from data.config import ADMINS, CHANNELS
from keyboards.inline.manage_post import confirmation_keyboard, post_callback
from loader import dp, bot
from states.poster import NewPost


@dp.message_handler(Command('create_post'))
async def get_channel_info(message: Message):
    await message.answer("Отправьте мне пост на публикацию")
    await NewPost.EnterMessage.set()


@dp.message_handler(state=NewPost.EnterMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer("Вы собираетесь отправить пост на проверку?",
                         reply_markup=confirmation_keyboard)
    await NewPost.next()


@dp.callback_query_handler(post_callback.filter(action='post'), state=NewPost.Confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        print(dict(data))
        print(data)
        text = data.get('text')
        mention = data.get('mention')

    await state.finish()
    await call.message.answer('Вы отправили пост на проверку')

    await bot.send_message(chat_id=ADMINS[0], text=f'Пользователь {mention} хочет сделать пост:')
    await bot.send_message(chat_id=ADMINS[0], text=text, parse_mode='HTML', reply_markup=confirmation_keyboard)


@dp.callback_query_handler(post_callback.filter(action='cancel'), state=NewPost.Confirm)
async def name_function(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer('Вы отклонили пост')


@dp.message_handler(state=NewPost.Confirm)
async def _post_unknown(message: Message):
    await message.answer('Выберите опубликовать или отклонить пост.')


@dp.callback_query_handler(post_callback.filter(action='post'), user_id=ADMINS)
async def approve_post(call: CallbackQuery):
    await call.answer("Вы одобрили этот пост", show_alert=True)
    target_channel = CHANNELS[0]

    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=target_channel)


@dp.callback_query_handler(post_callback.filter(action='cancel'), user_id=ADMINS)
async def decline_post(call: CallbackQuery):
    await call.answer('Вы отклонили этот пост.', show_alert=True)
    await call.message.edit_reply_markup()
