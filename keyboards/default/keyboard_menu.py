from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(text='Штаны'),
            ],
            [
                KeyboardButton(text='Кросовки'),
                KeyboardButton(text='Носки'),

            ],
        ],
        resize_keyboard=True
)
