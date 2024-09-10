from aiogram.fsm.state import State, StatesGroup


class TestConfigState(StatesGroup):
    lang = State()
    level = State()
    count = State()
