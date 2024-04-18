from pydantic import BaseModel


class CreatedBookModel(BaseModel):
    title: str
    author: str
    genre: str
    description: str
