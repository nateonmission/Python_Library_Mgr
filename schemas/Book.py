
from pydantic import BaseModel
from typing import Optional
from datetime import date

class Book(BaseModel):
    title : str
    author_id : int
    description : Optional[str]
    isbn_10 : Optional[str]
    isbn_13 : Optional[str]
    date_published : Optional[date]
    rating : Optional[int]


    class Config:
        orm_mode = True