from aiogram import Router, html
from aiogram.types import Message
from aiogram.filters import Command, CommandObject

from src.database import Genres, Books
from src.utils.others import get_form

router = Router(name="search_book")


@router.message(Command("search"))
async def search(message: Message, command: CommandObject):
    if command.args is None:
        return await message.answer(get_form(search.__name__))

    try:
        if ";" in command.args:
            title, author = command.args.split(";", maxsplit=1)
        else:
            title, author = command.args, None
    except ValueError:
        return await message.answer(get_form(search.name))

    author = author if author and len(author) > 2 else None

    if author:
        book = await Books.filter(title=title, author=author).first()
    else:
        book = await Books.filter(title=title).first()

    if not book:
        return await message.answer("ℹ️ <b>Не нашёл книгу в базе данных</b>")

    genre = await Genres.filter(id=book.genre_id).first()

    await message.answer(
        f"<b>Информация о книге</b> {html.code(book.title)}\n"
        f"ℹ️ <b>Автор:</b> {html.code(book.author)}\n"
        f"ℹ️ <b>Жанр:</b> {html.code(genre.genre)}\n"
        f"ℹ️ <b>Описание:</b> {html.unparse(book.description)}\n\n"
        f"<b>📀 Её ID в базе данных:</b> {html.code(book.id)}"
    )

