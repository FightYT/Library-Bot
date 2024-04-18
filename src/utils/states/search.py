from aiogram.fsm.state import State, StatesGroup


class Search(StatesGroup):
    entering_title = State()
    entering_author = State()
    entering_genre = State()
    confirm = State()
