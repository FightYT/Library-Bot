from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject

from src.database import Books
from src.utils.others import get_form

router = Router(name="keyword")


@router.message(Command("keyword"))
async def keyword(message: Message, command: CommandObject):
    if not command.args:
        return await message.answer(get_form(keyword.__name__))

    try:
        key_word = command.args[0]
    except ValueError:
        return await message.answer(get_form(keyword.__name__))

    try:
        books = await Books.raw(f"SELECT * FROM books WHERE title LIKE '%{key_word}%' OR author LIKE '%{key_word}%'")
    except Exception:
        return await message.answer(
            f"ℹ️ <b>Ошибка: При запросе к базе данных произошла ошибка. Повторите попытку позже</b>")

    if not books:
        return await message.answer(f"ℹ️ <b>Ошибка: По вашему ключевому слову в базе данных ничего не найдено</b>")

    list_of_books = "".join("{} - {}\n".format(book.title, book.author) for book in books)

    await message.answer(
        "📚 <b>Список книг в библиотеке по вашему ключевому слову:</b>\n"
        f"<b>Формат:</b> <code> Название - Автор</code>\n{list_of_books}")