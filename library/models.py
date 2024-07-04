from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author", back_populates="books")
    borrowers = relationship("Borrower", back_populates="book")

class Borrower(Base):
    __tablename__ = 'borrowers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'))
    book = relationship("Book", back_populates="borrowers")
