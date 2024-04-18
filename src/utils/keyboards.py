from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_confirm_kb() -> ReplyKeyboardMarkup:
    """
    :return: Возвращает клавиатуру подтверждения добавления книги (/add_book)
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Все верно")
            ],
            [
                KeyboardButton(text="Отмена")
            ]
        ],
        resize_keyboard=True
    )

    return keyboard


def get_search_kb() -> ReplyKeyboardMarkup:
    """
    :return: Возвращает клавиатуру поиска книги (/search)
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Пропустить")
            ],
            [
                KeyboardButton(text="Отмена")
            ]
        ],
        resize_keyboard=True
    )

    return keyboard


def get_cancel_kb() -> ReplyKeyboardMarkup:
    """
    :return: Возвращает клавиатуру отмены добавления книги (/add_book)
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Отмена")
            ]
        ],
        resize_keyboard=True
    )

    return keyboard
