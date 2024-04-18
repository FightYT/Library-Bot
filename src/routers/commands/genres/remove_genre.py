from aiogram import Router, html
from aiogram.types import Message
from aiogram.filters import Command, CommandObject

from src.database import Genres
from src.utils.others import get_form

router = Router(name="remove_genre")


@router.message(Command("remove_genre"))
async def remove_genre(message: Message, command: CommandObject):
    if command.args is None:
        return await message.answer(get_form(remove_genre.__name__))

    try:
        genre = command.args
    except ValueError:
        return await message.answer(get_form(remove_genre.__name__))

    base = await Genres.filter(genre=genre).first()
    if not base:
        await message.answer(f"ℹ️ <b>Жанр {html.code(genre)} не найден в базе данных.</b>")

    await base.delete()
    await message.answer(f"ℹ️ <b>Жанр {html.code(genre)} был успешно удалён из справочника.</b>")
