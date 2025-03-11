from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from typing import List
from src.books.books_data import books
from src.books.schemas import Book, BookUpdateModel

router = APIRouter()

@router.get("/", response_model=List[Book])
async def get_all_books():
    return books


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()
    books.routerend(new_book)
    return new_book


@router.get("/{book_id}")
async def get_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@router.patch("/{book_id}")
async def update_book(book_id: int, book_data: BookUpdateModel) -> dict:
    for book in books:
        if book["id"] == book_id:
            book['title'] = book_data.title
            book['author'] = book_data.author
            book['publisher'] = book_data.publisher
            book['page_count'] = book_data.page_count
            book['language'] = book_data.language
            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@router.delete("/{book_id}")
async def get_book(book_id: int) -> dict:
    for book in books: 
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully"}     
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
