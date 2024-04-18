from aiogram import Router

from .commands import start
from .commands.books import add_book, remove_book, search_book, \
                            keyword, books, books_genre
from .commands.genres import genres, add_genre, search_genre, remove_genre

routers: list[Router] = [
    start.router,
    books.router,
    add_book.router,
    remove_book.router,
    search_book.router,
    keyword.router,
    genres.router,
    add_genre.router,
    remove_genre.router,
    search_genre.router,
    books_genre.router
]


async def register_handlers(dispatcher: Router):
    for router in routers:
        dispatcher.include_router(router)
