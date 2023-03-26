from pydantic import BaseModel
from typing import Optional
from datetime import date

class Author(BaseModel):
    
    given_name : str
    family_name : str
    rating : Optional[int]

    class Config:
        orm_mode = True
