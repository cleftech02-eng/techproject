from fastapi import FastAPI
from pydantic import BaseModel

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