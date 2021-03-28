from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import ALLOWED_USERS
from loader import dp


@dp.inline_handler(text='')  # пустой запрос
async def empty_query(query: types.InlineQuery):
    await query.answer(
            results=[
                types.InlineQueryResultArticle(
                        id='unknown',
                        title='Введите какой-то запрос',
                        input_message_content=types.InputTextMessageContent(
                                message_text='Не обязательно жать на эту кнопку',

                        )

                )
            ],
            cache_time=5,
    )


@dp.inline_handler()  # пустой запрос
async def some_query(query: types.InlineQuery):
    user = query.from_user.id
    if user not in ALLOWED_USERS:
        await query.answer(
                results=[],
                switch_pm_text="Бот недоступен. Подключить бота",
                switch_pm_parameter='connect_user',
                cache_time=5,
        )
        return
    else:
        await query.answer(
                results=[
                    types.InlineQueryResultArticle(
                            id='1',
                            title='Название, которое отображается в инлайн режиме!',
                            input_message_content=types.InputTextMessageContent(
                                    message_text='Тут какой-то <b>text</b>, который будет '
                                                 'отправлен при нажатии на кнопку'
                            ),
                            url='https://core.telegram.org/bots/api#inlinequeryresult',
                            thumb_url='https://yandex-images.naydex.net/uP4t9E204/2dbb86T3dI/vKGNzcUk1RLpy6GESZ_q0xyW0qaW-xCH4IVqzs0scuHanJ0wrmmG3gHufGwLIerbOoDFYjcUMt2ul7egyUZmWKrqhoTdIZZCrJnlxDjH65UKioDxw_hQnLrUf9TILGX8kcySDfIplpJRtyEAAiPtxBWq5nxALki3hLbN3dJGbVipqpmQnxr8U9j6p4IAoOLkdZXagZHWLfzNlU2G_jlQjdO2mC2FfqyWarwqBUlDrr8wpd9YbAZFjqml0cXkaVtSvZjjuJAE6RD8zYuUCof672a_2KSj5D7nxph5ldsjTZjikbUCrG-Vi16uPAheX6SOM5LAd0saTIyml9fQ6GxSc7m4-5GQNsgm-M-5kAyV4-dWmde-ofA62N2zR6nyHWqeya6RB4R_toVfjwUVS0G6gDCl4VRDFnGCv6Lq-t1Ea2iWg9uArwLlFcXCorY9g__td7jmp7r1D8_pgX-Q-j9Ogve8igG5cauDfqgnEWd8uoQgotZPVTlBlqyw_eDASUtem7zbp5420Tvnz4eyP6HBxkiO3qef1QX8yqdHr8YbVKrmq54jiWyxhHiLAiViRYuCJo_CZ1orc7yXmsz33VNRRoGw-IakMvIq0O-ivxSc4Nhag9uagMYc0Pm5Tq_yAmiB8IypDJtyiYNglxMXXEWOpD6n5XlvM3Sst77I1uFTVFO0huakmw7NAvHPma4Fos_uYoj9mb3MItDihnOC-SJ2h9aguieiYL2JZqosC31ZnpMatNB-SjVwpLig4d_OdVNmibHBiqQP7RLQ7p2SIZHhwkWF35uF_RrIxa93mOgPY43pgLo2i1SDsFuQBi55aZK4BaH9ZXUgY6q1msbZ_lVRTp2j2YWsLMkB8POKtgOLysxYtdiAuOYR-92TTbHCH0mnzYC0H6VljoFCgT0scFavggWZ_XV2NnGEgqDD3cdtQEuouvyxgAj6N-n8tL4Ptf7sUbnbr5bfG8zWtXuj3g0',
                            description='Описание в inline режиме',
                    ),
                    types.InlineQueryResultVideo(
                            id='4',
                            video_url='https://vod-progressive.akamaized.net/exp=1616984858~acl=%2A%2F1184362465.mp4%2A~hmac=724e6a51624b783d8501bb6728806750c5534fa8cfcf979478aa87ab39842397/vimeo-prod-skyfire-std-us/01/1629/12/308149231/1184362465.mp4?download=1&filename=Pexels+Videos+1722593.mp4',
                            caption='Подпись к видео',
                            title='Какое то видео',
                            description='Какое то описание',
                            thumb_url='https://cs11.pikabu.ru/post_img/big/2020/07/11/6/1594455152112121353.jpg',
                            mime_type='video/mp4',  # text/html

                    )
                ]
        )


@dp.message_handler(CommandStart(deep_link='connect_user'))
async def connect_user(message: types.Message):
    ALLOWED_USERS.append(message.from_user.id)
    await message.answer('Вы подключены',
                         reply_markup=InlineKeyboardMarkup(
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text='Войти в inline режим',
                                                              switch_inline_query_current_chat='Запрос')
                                     ]
                                 ]
                         ))
