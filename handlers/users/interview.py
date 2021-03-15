from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types
from states import Interview


# Старт quiz
@dp.message_handler(Command('interview'), state=None)
async def start_interview(msg: types.Message):
    await msg.answer('Вы начали тестирование\n'
                     '\n'
                     'Вопрос №1.\n\n'
                     'Как вас зовут?')

    await Interview.question_one.set()
    # await Interview.first()


@dp.message_handler(state=Interview.question_one)
async def question_one(msg: types.Message, state: FSMContext):
    """
    example.
    вариант 1:
        await state.update_data(answer_one=answer)

    вариант 2:
        await state.update_data({
            'answer_one': answer
        })
    вариант 3:
        async with state.proxy() as data:
            data['answer_one'] = answer
    """
    answer = msg.text

    async with state.proxy() as data:
        data['answer_name'] = answer

    await msg.answer(f'Вы указали ваше имя: {answer}\n\nВопрос №2.\n\n'
                     'Ваш возраст?')

    await Interview.question_two.set()


@dp.message_handler(state=Interview.question_two)
async def question_two(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    answer_age = msg.text
    answer_name = data.get('answer_name')

    async with state.proxy() as data:
        data['answer_age'] = answer_age

    await msg.answer(f'Вы указали ваше имя: {answer_name}\n'
                     f'Вы указали ваш возраст: {answer_age}\n\n'
                     f'Вопрос №3.\n\n'
                     f'Ваш телефон?')

    # await Interview.question_tree.set()
    await Interview.next()
    # await Interview.previous()


@dp.message_handler(state=Interview.question_tree)
async def question_tree(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer_phone = msg.text
        data['answer_phone'] = answer_phone

    await msg.answer(f'Вы указали ваше имя: {data["answer_name"]}\n'
                     f'Вы указали ваш возраст: {data["answer_age"]}\n'
                     f'Вы указали ваш телефон: {answer_phone}\n'
                     f'Спасибо за ваши ответы.\n\n')

    # await state.finish()
    # await state.reset_state(with_data=False)  # не сбрасывает данные но состояние
    await state.reset_state()


#
#
#
# example


# Можно использовать вместо группы состояний определенный единичный стейт
@dp.message_handler(state='enter_email')
async def enter_email(msg: types.Message, state: FSMContext):
    await msg.answer(f'Ваш Email {msg.text}')
    await state.finish()


@dp.message_handler(Command('email'))
async def mail(msg: types.Message, state: FSMContext):
    await msg.answer('Что то отвечаем')
    await state.set_state('enter_email')
