from src.models.schemas import BookCreate, Book
from src.modules.fake_db import books

FAKER_BOOKS = books


def create_book(book: BookCreate):
    book_id = len(FAKER_BOOKS) + 1
    db_book = Book(id=book_id, **book.dict())
    FAKER_BOOKS[book_id] = db_book
    return db_book
