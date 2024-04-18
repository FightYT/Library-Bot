from aiogram import Router, html
from aiogram.types import Message
from aiogram.filters import Command, CommandObject

from src.database import Genres
from src.utils.others import get_form

router = Router(name="add_genre")


@router.message(Command("add_genre"))
async def add_genre(message: Message, command: CommandObject):
    if command.args is None:
        return await message.answer(get_form(add_genre.__name__))

    try:
        genre = command.args
    except ValueError:
        return await message.answer(get_form(add_genre.__name__))

    base = await Genres.filter(genre=genre).first()
    if base:
        return await message.answer(f"ℹ️ <b>Жанр {html.code(genre)} уже есть в справочнике.</b>")

    await Genres.create(genre=genre)
    await message.answer(f"ℹ️ <b>Жанр {html.code(genre)} был успешно добавлен в справочник.</b>")
