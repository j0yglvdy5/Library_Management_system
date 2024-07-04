
import click
from library.db import SessionLocal, engine, Base
from library.models import Author, Book, Borrower

Base.metadata.create_all(bind=engine)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
def create_author(name):
    db = SessionLocal()
    author = Author(name=name)
    db.add(author)
    db.commit()
    click.echo(f"Author '{author.name}' added with ID {author.id}.")
    db.close()

@cli.command()
@click.argument('title')
@click.argument('author_id', type=int)
def create_book(title, author_id):
    db = SessionLocal()
    author = db.query(Author).filter(Author.id == author_id).first()
    if author:
        book = Book(title=title, author_id=author_id)
        db.add(book)
        db.commit()
        click.echo(f"Book '{book.title}' added with ID {book.id} and Author ID {book.author_id}.")
    else:
        click.echo(f"Author with ID {author_id} not found.")
    db.close()

@cli.command()
@click.argument('name')
@click.argument('email')
def create_borrower(name, email):
    db = SessionLocal()
    borrower = Borrower(name=name, email=email)
    db.add(borrower)
    db.commit()
    click.echo(f"Borrower '{borrower.name}' added with ID {borrower.id}.")
    db.close()

@cli.command()
def list_authors():
    db = SessionLocal()
    authors = db.query(Author).all()
    for author in authors:
        click.echo(f"ID: {author.id}, Name: {author.name}")
    db.close()

@cli.command()
def list_books():
    db = SessionLocal()
    books = db.query(Book).all()
    for book in books:
        click.echo(f"ID: {book.id}, Title: {book.title}, Author ID: {book.author_id}")
    db.close()

@cli.command()
def list_borrowers():
    db = SessionLocal()
    borrowers = db.query(Borrower).all()
    for borrower in borrowers:
        click.echo(f"ID: {borrower.id}, Name: {borrower.name}, Email: {borrower.email}")
    db.close()

if __name__ == '__main__':
    cli()
