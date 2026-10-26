from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

app = FastAPI()

class Book(BaseModel):
    id : str
    title : str
    author: str
    year : int
    page : int
    language : str

class Book_create(BaseModel):
    title : str
    author: str
    year : int
    page : int
    language : str

class Bookupdate(BaseModel):
     title : str
     author: str
     year : int
     page : int
     language : str

class Books(BaseModel):
    books : List[Book]

class Response(BaseModel):
    message : Optional[str] = None
    has_error : bool = None
    error_message: Optional[str] = None
    data : Optional[Book| Books] 

books : dict[str, Books] = {}

@app.get("/")
def home ():
    return {"message" : "hello from the books API"}

@app.get("/books")
def get_books():
    return books

@app.get("/book/{id}")
def get_books(id: UUID):
    book = books.get(str(id))
    if not book:
        return {"error":"Book not found"}
    return book

@app.post("/book")
def post_books(book_in:Book_create):
    book = Book(
        id=str(uuid4()), **book_in.model_dump()
        )
    books[book.id] = book
    return Response(message = "Book added successfully", data= book)

@app.put("/books/{id}")
def update_book(id:UUID, book_in:Bookupdate):
    book = books.get(str(id))
    if not book:
        return{"error": "Book not found"}
    book.title = book_in.title
    book.pages = book_in.pages
    book.language = book_in.language

    return Response(message="book update successfully")
_
