import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from schemas.Book import Book as Book_Schema
from schemas.Author import Author as Author_Schema
from models.Book import Book as Book_Model
from models.Author import Author as Author_Model

load_dotenv(".env")

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

@app.get("/")
async def root():
    return {"message": "Server is UP"}

@app.post("/library/v0/book", response_model=Book_Schema)
def create_book(book: Book_Schema):
    db_book = Book_Model(title=book.title, author_id=book.author_id)
    db.session.add(db_book)
    db.session.commit()
    return db_book

@app.post("/library/v0/author", response_model=Author_Schema)
def create_author(author: Author_Schema):
    print(author)
    db_author = Author_Model(given_name=author.given_name, family_name=author.family_name)
    db.session.add(db_author)
    db.session.commit()
    return db_author