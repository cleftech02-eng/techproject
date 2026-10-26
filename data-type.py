from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Book(BaseModel):
    id : int
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
    message : Optional[str]
    
