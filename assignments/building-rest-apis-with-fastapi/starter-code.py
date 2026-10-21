from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Book Collection API")


class Book(BaseModel):
    id: int
    title: str
    author: str


class BookInput(BaseModel):
    title: str
    author: str


books: dict[int, Book] = {}
next_book_id = 1
