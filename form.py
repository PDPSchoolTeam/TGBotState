from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    name = State()
    age = State()
    gender = State()
    birthday = State()
    password = State()
    finish = State()
