
import click
from sqlalchemy.orm import Session
from library.db import SessionLocal, engine
from library.models import Author, Book, Borrower
from library.services import create_author, create_book, create_borrower

Author.metadata.create_all(bind=engine)

@click.group()

def cli():
    pass

@cli.command()
@click.argument('name')
def create_author_cmd(name):
    db = SessionLocal()
    author = create_author(db, name)
    click.echo(f"Author '{author.name}' added with ID {author.id}.")
    db.close()

@cli.command()
@click.argument('title')
@click.argument('author_id', type=int)
def create_book_cmd(title, author_id):
    db = SessionLocal()
    author = db.query(Author).filter(Author.id == author_id).first()
    if author:
        book = create_book(db, title, author_id)
        click.echo(f"Book '{book.title}' added with ID {book.id} and Author ID {book.author_id}.")
    else:
        click.echo(f"Author with ID {author_id} not found.")
    db.close()

@cli.command()
@click.argument('name')
@click.argument('email')
def create_borrower_cmd(name, email):
    db = SessionLocal()
    borrower = create_borrower(db, name, email)
    click.echo(f"Borrower '{borrower.name}' added with ID {borrower.id}.")
    db.close()

if __name__ == '__main__':
    cli()
