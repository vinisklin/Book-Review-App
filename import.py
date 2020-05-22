import os
from numpy import genfromtxt
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# Make a list with all books in CSV file
books = genfromtxt('books.csv', delimiter=',', dtype=("|S10", "|S32", "|S32", int), skip_header=1, loose=True,
                   invalid_raise=False).tolist()

for book in books:
    # Cast variables to respective DB formats
    title = str(book[1]).strip("b'")
    author = str(book[2]).strip("b'")
    year = book[3]
    isbn = str(book[0]).strip("b'")

    # Check if isbn already exists in DB
    if db.execute("SELECT * FROM books_table WHERE isbn = :isbn", {"isbn": isbn}).rowcount == 0:
        # Add book info to DB
        db.execute("INSERT INTO books_table (title, author, year, isbn) VALUES (:title, :author, :year, :isbn)",
                   {"title": title, "author": author, "year": year, "isbn": isbn})
        db.commit()
