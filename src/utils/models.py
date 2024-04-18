from pydantic import BaseModel


class CreatedBookModel(BaseModel):
    """
    Модель данных созданной книги (/add_book)

    Attributes:
        title (str): Название книги
        author (str): Автор книги
        genre (str): Название жанра
        description (str): Описание книги
    """
    title: str
    author: str
    genre: str
    description: str
