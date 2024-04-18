from aiogram import Router, html
from aiogram.types import Message
from aiogram.filters import Command, CommandObject

from src.database import Genres, Books
from src.utils.others import get_form

router = Router(name="books_genre")

@router.message(Command("books_genre"))
async def books_genre(message: Message, command: CommandObject):
    if command.args is None:
        return await message.answer(get_form(books_genre.__name__))

    genres = await Genres.filter(genre=command.args).first()
    if not genres:
        return await message.answer("📚 <b> Нет в списке такого жанра</b>")

    books = await Books.filter(genre_id=genres.id)
    if not books:
        return await message.answer("📚 <b> В библиотеке нет книг с таким жанром</b>")

    list_of_books = "".join("{} - {}\n".format(html.code(book.title), html.code(book.author)) for book in books)

    await message.answer(
        f"📚 <b>Список книг в библиотеке с жанром <code>{genres.genre}</code>:</b>\n"
        f"<b>Формат:</b> <code> Название - Автор</code>\n{list_of_books}"
        "\n\n<b>Что узнать описание, найдите книгу с помощью команды</b> /search")