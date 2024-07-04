from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import Session,relationship
from .db import Base, SessionLocal

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    @classmethod
    def get_all(cls, session: Session = SessionLocal()):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, author_id: int, session: Session = SessionLocal()):
        return session.query(cls).filter(cls.id == author_id).first()
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))

    author = relationship("Author", back_populates="books")

    @classmethod
    def get_all(cls, session: Session = SessionLocal()):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, book_id: int, session: Session = SessionLocal()):
        return session.query(cls).filter(cls.id == book_id).first()

class Borrower(Base):
    __tablename__ = 'borrowers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, unique=True)

    @classmethod
    def get_all(cls, session: Session = SessionLocal()):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, borrower_id: int, session: Session = SessionLocal()):
        return session.query(cls).filter(cls.id == borrower_id).first()
