from aiogram import Router, html, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, StateFilter, CommandObject
from aiogram.fsm.context import FSMContext

from src.database import Genres, Books
from src.utils.states import AddBook
from src.utils.models import CreatedBookModel
from src.utils.keyboards import get_cancel_kb, get_confirm_kb
from src.utils.others import get_form

router = Router(name="remove_book")


@router.message(Command("remove_book"))
async def remove_book(message: Message, command: CommandObject):
    if not command.args:
        return await message.answer(get_form(remove_book.__name__))

    try:
        title, author = command.args.split(";", maxsplit=1)
    except ValueError:
        return await message.answer(get_form(remove_book.__name__))

    book = await Books.filter(title=title, author=author).first()
    if not book:
        return await message.answer(f"ℹ️ <b>Ошибка: Книга не найдена в базе данных.</b>")

    await book.delete()
    await message.answer(f"<b>ℹ️ Книга </b> {html.code(book.title)} <b>автора</b> {html.code(book.author)} "
                         f"<b>была удалена из базы данных.</b>")