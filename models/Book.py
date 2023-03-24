from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .Author import Author

Base = declarative_base

class Book():
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(127))
    description = Column(String(255))
    isbn_10 = Column(String(15))
    isbn_13 = Column(String(20))
    date_published = Column(DateTime)
    rating = Column(Integer)
    created_timestamp = Column(DateTime(timezone=True), server_default=func.now())
    late_update_timestamp = Column(DateTime(timezone=True), onupdate=func.now())
    author_id = Column(Integer, ForeignKey("author.id"))

    author = relationship("Author")