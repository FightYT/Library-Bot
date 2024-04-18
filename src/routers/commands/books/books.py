from aiogram import Router, html
from aiogram.types import Message
from aiogram.filters import Command

from src.database import Books

router = Router(name="books")


@router.message(Command("books"))
async def get_books(message: Message):
    books = await Books.all()
    if not books:
        return await message.answer("📚 <b> В библиотеке нет книг</b>")

    list_of_books = "".join("{} - {}\n".format(html.code(book.title), html.code(book.author)) for book in books)

    await message.answer(
        "📚 <b>Список книг в библиотеке:</b>\n"
        f"<b>Формат:</b> <code> Название - Автор</code>\n{list_of_books}"
        "\n\n<b>Что узнать описание, найдите книгу с помощью команды</b> /search")
        
