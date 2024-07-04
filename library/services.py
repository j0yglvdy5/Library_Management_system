
from sqlalchemy.orm import Session
from .models import Author, Book, Borrower
from .db import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def add_author(name: str):
    db = SessionLocal()
    author = Author(name=name)
    db.add(author)
    db.commit()
    db.refresh(author)
    db.close()
    return author

def add_book(title: str, author_id: int):
    db = SessionLocal()
    book = Book(title=title, author_id=author_id)
    db.add(book)
    db.commit()
    db.refresh(book)
    db.close()
    return book

def add_borrower(name: str, book_id: int):
    db = SessionLocal()
    borrower = Borrower(name=name, book_id=book_id)
    db.add(borrower)
    db.commit()
    db.refresh(borrower)
    db.close()
    return borrower

def list_authors():
    db = SessionLocal()
    authors = db.query(Author).all()
    db.close()
    return authors

def list_books():
    db = SessionLocal()
    books = db.query(Book).all()
    db.close()
    return books

def list_borrowers():
    db = SessionLocal()
    borrowers = db.query(Borrower).all()
    db.close()
    return borrowers

def delete_author(author_id: int):
    db = SessionLocal()
    author = db.query(Author).filter(Author.id == author_id).first()
    if not author:
        raise ValueError("Author not found")
    db.delete(author)
    db.commit()
    db.close()

def delete_book(book_id: int):
    db = SessionLocal()
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise ValueError("Book not found")
    db.delete(book)
    db.commit()
    db.close()

def delete_borrower(borrower_id: int):
    db = SessionLocal()
    borrower = db.query(Borrower).filter(Borrower.id == borrower_id).first()
    if not borrower:
        raise ValueError("Borrower not found")
    db.delete(borrower)
    db.commit()
    db.close()

def find_author_by_name(name: str):
    db = SessionLocal()
    author = db.query(Author).filter(Author.name == name).first()
    db.close()
    return author

def find_book_by_title(title: str):
    db = SessionLocal()
    book = db.query(Book).filter(Book.title == title).first()
    db.close()
    return book

def find_borrower_by_name(name: str):
    db = SessionLocal()
    borrower = db.query(Borrower).filter(Borrower.name == name).first()
    db.close()
    return borrower
