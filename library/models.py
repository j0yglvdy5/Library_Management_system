
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from library.db import Base

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    books = relationship('Book', back_populates='author')

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)

    author = relationship('Author', back_populates='books')

class Borrower(Base):
    __tablename__ = 'borrowers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
