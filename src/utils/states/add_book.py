from aiogram.fsm.state import State, StatesGroup


class AddBook(StatesGroup):
    entering_book_name = State()
    entering_book_author = State()
    entering_book_genre = State()
    entering_book_description = State()
    confirm = State()
