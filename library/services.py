from sqlalchemy.orm import Session
from .models import Author, Book, Borrower
from .db import SessionLocal

def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()

def create_author(db: Session, name: str):
    author = Author(name=name)
    db.add(author)
    db.commit()
    db.refresh(author)
    return author

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, title: str, author_id: int):
    book = Book(title=title, author_id=author_id)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_borrower(db: Session, borrower_id: int):
    return db.query(Borrower).filter(Borrower.id == borrower_id).first()

def create_borrower(db: Session, name: str, email: str):
    borrower = Borrower(name=name, email=email)
    db.add(borrower)
    db.commit()
    db.refresh(borrower)
    return borrower


