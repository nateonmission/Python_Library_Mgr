from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

AuthorBase = declarative_base()

class Author(AuthorBase):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True, index=True)
    given_name = Column(String)
    family_name = Column(String)
    rating = Column(Integer)
    created_timestamp = Column(DateTime(timezone=True), server_default=func.now())
    late_update_timestamp = Column(DateTime(timezone=True), onupdate=func.now())
