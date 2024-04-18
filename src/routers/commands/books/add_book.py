from aiogram import Router, F, html
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from src.database import Genres, Books
from src.utils.states import AddBook
from src.utils.models import CreatedBookModel
from src.utils.keyboards import get_cancel_kb, get_confirm_kb

router = Router(name="add_book")


@router.message(StateFilter(None), Command("add_book"))
async def add_book(message: Message, state: FSMContext):
    await message.answer(
        "📚 <b>Для добавления книжки вам необходимо указать</b> "
        "<code>название, автора, жанр и описание</code>\n"
        "🧨️ <b>Бот будет поочередно спрашивать у вас информацию</b>\n\n"
        "✍️ Пожалуй начнём: <code>укажите название кники</code>\n\n"
        "🚫 <code>Если что-то пойдёт не так</code> - <b>нажмите на кнопку Отмена</b>",
        reply_markup=get_cancel_kb()
    )
    await state.set_state(AddBook.entering_book_name)


@router.message(AddBook.entering_book_name, F.text != "Отмена")
async def handle_book_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer(
        "📚 <b>Отлично.</b> <code>Теперь укажите автора:</code>",
        reply_markup=get_cancel_kb())
    await state.set_state(AddBook.entering_book_author)


@router.message(AddBook.entering_book_author, F.text != "Отмена")
async def handle_book_author(message: Message, state: FSMContext):
    await state.update_data(author=message.text)

    base = await Genres.all()
    genres = "".join([row.genre + "\n" for row in base])

    await message.answer(
        "📚 <b>Теперь укажите жанр</b>\n"
        f"💼 <code>Справочник жанров:</code> \n{genres}\n"
        "<b>✍️ Если жанра нет в списке - все равно введите его, он будет занесён в базу данных</b>",
        reply_markup=get_cancel_kb()
    )
    await state.set_state(AddBook.entering_book_genre)


@router.message(AddBook.entering_book_genre, F.text != "Отмена")
async def handle_book_genre(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)
    await message.answer(
        "📚 <b>Теперь укажите описание книги:</b>",
        reply_markup=get_cancel_kb())
    await state.set_state(AddBook.entering_book_description)


@router.message(AddBook.entering_book_description, F.text != "Отмена")
async def handle_book_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    form = CreatedBookModel(**await state.get_data())

    await message.answer(
        "🔎 <b> Проверьте введенную информацию:</b>\n\n"
        f"ℹ️ <b>Название:</b> {html.code(form.title)}\n"
        f"ℹ️ <b>Автор:</b> {html.code(form.author)}\n"
        f"ℹ️ <b>Жанр:</b> {html.code(form.genre)}\n"
        f"ℹ️ <b>Описание:</b> {html.unparse(form.description)}\n\n"
        "😊 <b>Если всё верно - нажмите на кнопку \"Все верно\"</b>\n"
        "🚫 <b>Если вы допустили ошибку - нажмите на кнопку \"Отменить\"</b>",
        reply_markup=get_confirm_kb()
    )
    await state.set_state(AddBook.confirm)


@router.message(StateFilter(None), F.text == "Отмена")
async def cmd_cancel_no_state(message: Message, state: FSMContext):
    await state.set_data({})
    await message.answer(
        text=f"ℹ️ <b>Отменять нечего.</b>",
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(AddBook.confirm, F.text == "Все верно")
async def confirm_yes(message: Message, state: FSMContext):
    form = CreatedBookModel(**await state.get_data())

    base = await Genres.filter(genre=form.genre).first()
    if not base:
        # Если жанра нет в БД заносим его
        base = await Genres.create(genre=form.genre)
        await message.answer(
            f"ℹ️ <b>Система автоматически занесла жанр</b> {html.code(form.genre)} "
            f"<b>в список жанров.</b>")

    book = await Books.create(
        title=form.title, author=form.author,
        genre_id=base.id, description=form.description
    )
    await message.answer(
        f"🔎 <b>Вы успешно внесли книгу в базу данных:\nВот информация о ней:\n</b>"
        f"ℹ️ <b>Название:</b> {html.code(form.title)}\n"
        f"ℹ️ <b>Автор:</b> {html.code(form.author)}\n"
        f"ℹ️ <b>Жанр:</b> {html.code(form.genre)}\n"
        f"ℹ️ <b>Описание:</b> {html.unparse(form.description)}\n\n"
        f"<b>📀 Её ID в базе данных:</b> {html.code(book.id)}",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.clear()


@router.message(F.text == "Отмена")
async def confirm_no(message: Message, state: FSMContext):
    await message.answer(
        f"ℹ️ <b>Вы отменили добавление книжки</b>",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.clear()
