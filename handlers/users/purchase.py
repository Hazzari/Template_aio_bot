from aiogram import types
from aiogram.dispatcher.filters import Command
from loguru import logger

from keyboards.inline.calback_datas import buy_callback
from keyboards.inline.choice_button import choice_item, sneakers_keyboard
from keyboards.inline.choice_button import jacket_keyboard
from loader import dp, bot


@dp.message_handler(Command('items'))
async def show_items(message: types.Message):
    await message.answer(text="На продажу есть 3 товара: 2 куртки, 5 штанов и кросовки.\n"
                              "если покупка не интересует жми отмену.",
                         reply_markup=choice_item)


@dp.callback_query_handler(buy_callback.filter(item_name='jacket'))
async def buy_jacket(call: types.CallbackQuery, callback_data: dict):
    # await bot.answer_callback_query(callback_query_id=callback.id) # тоже самое что и следующее
    await call.answer(cache_time=60)
    logger.info(f'callback_data = {call.data}')
    logger.info(f'callback_data dict = {callback_data}')
    quantity = callback_data.get('quantity')
    await call.message.answer(f'Вы выбрали купить куртку.\n'
                              f'Всего - {quantity}.\n'
                              f'Спасибо.\n',
                              reply_markup=jacket_keyboard)


@dp.callback_query_handler(buy_callback.filter(item_name='sneakers'))
async def buy_sneakers(call: types.CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logger.info(f'callback_data = {call.data}')
    logger.info(f'callback_data dict = {callback_data}')
    quantity = callback_data.get('quantity')
    await call.message.answer(f'Вы выбрали купить кросовки.\n'
                              f'Всего - {quantity}.\n'
                              f'Спасибо.\n', )


@dp.callback_query_handler(text='cancel')
async def cancel_buying(call: types.CallbackQuery):
    await call.answer('Вы отменили покупку', show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)
    #
    # await bot.edit_message_reply_markup(chat_id=call.from_user.id,
    #                                     message_id=call.message.message_id,
    #                                     reply_markup=None)
