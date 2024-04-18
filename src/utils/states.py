from aiogram.fsm.state import State, StatesGroup


class AddBook(StatesGroup):
    """
    Cостояний для команды добавления книги (/add_book).

    Attributes:
        entering_book_name (State): Состояние ввода названия книги.
        entering_book_author (State): Состояние ввода автора книги.
        entering_book_genre (State): Состояние ввода жанра книги.
        entering_book_description (State): Состояние ввода описания книги.
        confirm (State): Состояние подтверждения добавления книги.
    """
    entering_book_name = State()
    entering_book_author = State()
    entering_book_genre = State()
    entering_book_description = State()
    confirm = State()
