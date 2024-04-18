from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject

from src.database import Genres, Books
from src.utils.others import get_form

router = Router(name="search_genre")


@router.message(Command("search_genre"))
async def search_genre(message: Message, command: CommandObject):
    if command.args is None:
        return await message.answer(get_form(search_genre.__name__))

    try:
        genre = command.args
    except ValueError:
        return await message.answer(get_form(search_genre.__name__))

    base = await Genres.filter(genre=genre).first()
    if not base:
        return await message.answer("ℹ️ <b>Указанный жанр не найден в базе данных.</b>")

    books = await Books.filter(genre_id=base.id).all()

    list_of_books = "".join("{} - {}\n".format(book.title, book.author) for book in books)
    await message.answer(
        "📚 <b>Список книг в библиотеке:</b>\n"
        f"<b>Формат:</b> <code> Название - Автор</code>\n{list_of_books}")
