from aiogram import Router, html
from aiogram.types import Message
from aiogram.filters import Command

router = Router(name="start_cmd")


@router.message(Command("start", "help"))
async def start(message: Message):
    await message.answer(
        f"✌️ Привет, {html.bold(message.from_user.full_name)}\n"
        "📚 Я, бот библиотекарь, вот список моих команд:\n"
        "<b>Операции с книгами:</b>\n"
        "ℹ️ /books - <b>Список книг</b>\n"
        "ℹ️ /add_book - <b>Добавить книгу</b>\n"
        "ℹ️ /remove_book <code>[название];[автор]</code> - <b>Удалить книгу</b>\n"
        "ℹ️ /keyword <code>[слово]</code> - <b>Поиск по ключевому слову</b>\n"
        "ℹ️ /search <code>[название];[автор (опционально)]</code> - <b>Поиск по названию и жанру книги</b>\n\n"
        "<b>Операции с жанрами:</b>\n"
        "️️ℹ️ /books_genre <code>[жанр]</code> - <b>Список книг по жанру</b>\n"
        "ℹ️ /books - <b>Список книг</b>\n"
        "ℹ️ /genres - <b>Список жанров</b>\n"
        "ℹ️ /add_genre [жанр] - <b>Добавить жанр</b>\n"
        "ℹ️ /remove_genre [название] - <b>Удалить жанр</b>\n\n"
        "<b>Прочие команды:</b>\n"
        "ℹ️ /help - Вывести данный список"
    )
