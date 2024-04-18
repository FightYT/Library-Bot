from tortoise import fields
from tortoise.models import Model


class Genres(Model):
    """
    Таблица для хранения жанров книг.

    Attributes:
        id (int): Идентификатор жанра (первичный ключ)
        genre: (str): Название жанра.
    """
    id = fields.IntField(pk=True)

    genre = fields.CharField(max_length=128)

    class Meta:
        table = "genres"
