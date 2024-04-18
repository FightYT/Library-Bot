from tortoise import fields
from tortoise.models import Model


class Books(Model):
    """
    Таблица для хранения книг в библиотеке.

    Attributes:
        id (int): Идентификатор книги (первичный ключ)
        title: (str): Название книги.
        author: (str): Автор книги.
        genre_id: (int): Идентификатор жанра книги (Из таблицы genres).
        description: (str): Описание книги.
    """
    id = fields.IntField(pk=True)

    title = fields.CharField(max_length=256)
    author = fields.CharField(max_length=256)

    genre_id = fields.IntField()
    description = fields.CharField(max_length=2048)

    class Meta:
        table = "books"
