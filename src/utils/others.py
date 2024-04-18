forms: dict = {
    "books_genre": "/books_genre <code>[жанр]</code>",
    "keyword": "/keyword <code>[слово]</code>",
    "search": "/search <code>[название];[автор (опционально)]</code>",
    "remove_book": "/remove_book <code>[название];[автор]</code>",
    "add_genre": "/keyword <code>[жанр]</code>",
    "remove_genre": "/remove_genre <code>[жанр]</code>",
    "search_genre": "/search_genre <code>[жанр]</code>",

}


def get_form(command: str) -> str:
    """
    Получение правильной формы команды (Дабы не засорять код лишними строками)

    :param command: str - Название команды
    :return: Возвращает форму команды
    """
    return "ℹ️ <b>Ошибка: Правильное использование команды:</b>\n"+forms[command]
