from aiogram import Router, html
from aiogram.types import Message
from aiogram.filters import Command

from src.database import Genres

router = Router(name="genres")


@router.message(Command("genres"))
async def genres(message: Message):
    all_genres = await Genres.all()
    if not all_genres:
        return await message.answer("📚 <b> В справочнике нет жанров.</b>")

    list_of_books = "".join("{}\n".format(html.code(genre.genre)) for genre in all_genres)

    await message.answer(f"📚 <b>Список жанров в справочнике:</b>\n{list_of_books}")
