from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

check_button = InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(text='Проверить подписки на каналы', callback_data='check_subs'),

            ],
        ]
)
