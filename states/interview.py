from aiogram.dispatcher.filters.state import StatesGroup, State


class Interview(StatesGroup):
    question_one = State()
    question_two = State()
    question_tree = State()
