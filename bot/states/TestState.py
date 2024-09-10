from aiogram.fsm.state import State, StatesGroup


class TestState(StatesGroup):
    test = State()
    index = State()
    correct = State()
    count = State()
