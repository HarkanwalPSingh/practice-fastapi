from fastapi import APIRouter, HTTPException, status

from src.accessors.book_accessor import create_book
from src.models.schemas import Book, BookCreate

router = APIRouter(
    prefix="/books",
    tags=["books"]
)


@router.post("/", response_model=Book)
async def create_new_book(book: BookCreate):
    new_book = create_book(book)
    if not new_book:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid collection id")
    return new_book
