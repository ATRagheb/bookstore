
from fastapi import FastAPI
from src.books.routes import router as book_router

version = "v1"

app = FastAPI(
    title="bookly",
    version=version,
    description="A rest api for a book review app"
)

app.include_router(router=book_router, prefix=f'/api/{version}/books', tags=["books"])

