from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.calback_datas import buy_callback

# 2 способа создать кнопки
# 1-й способ:

choice_item = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Купить куртку',
                                     callback_data=buy_callback.new(item_name='jacket', quantity=1, color='yellow')),
                InlineKeyboardButton(text='Купить штаны', callback_data='buy:pants:1:black'),
                InlineKeyboardButton(text='Купить кросовки', callback_data='buy:sneakers:1:blue', ),
            ],
            [
                InlineKeyboardButton(text='Отмена', callback_data='cancel')
            ]
        ]
)

# 2-й способ
jacket_keyboard = InlineKeyboardMarkup(row_width=2)
JACKET_URL = 'https://www.finn-flare.ru/catalog/kurtki-zhenskie/444647/2155/'
jacket_url = InlineKeyboardButton(text='Купить куртку тут', url=JACKET_URL)
jacket_keyboard.insert(jacket_url)

sneakers_keyboard = InlineKeyboardMarkup()
sneakers_url = InlineKeyboardButton(text='Вы хотите купить кросовки', url=JACKET_URL)
sneakers_keyboard.insert(sneakers_url)
