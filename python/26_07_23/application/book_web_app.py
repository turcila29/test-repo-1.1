"""
Task for this afternoon: 
using the solution to the OOP exercise from yesterday (the book class),
create a flask app which allows users to:

add new books with information supplied via url/query params
search for books by a given author
update books that have already been added (stretch goal)
delete books from the system (stretch goal)
"""
from flask import Flask
from flask import request
from exercise2 import Book
from exercise2 import BookList
app = Flask(__name__)

def book_structure(book):
    return {
        "title": book.title,
        "pages": book.pages,
        "genre": book.genre,
        "by": book.author,
        "isbn": book.isbn
    }

books = BookList(
    Book("John Johnson", "Book Title", "200", "1235433865"),
    Book("Dorothy", "The wonderful world of os", "67", "904757363")
)


def get_args():
    return {key: value for key, value in request.args.items() if key in ("title", "author", "pages", "isbn")}

@app.route("/")


def index():
    return'''
    Welcome to the ultimate library experience<br>
    Guide:<br>
    /search --> search for books by author<br>
    /create --> add new book

'''

@app.route('/create')
def create():
    if request.args.get("isbn") in map(lambda b: b.isbn, Book.books):
        return f"{request.args.get('isbn')} is already in use", 403
    book = Book(**request.args, fromrepr=True)
    return f"added new book: {str(book)}"


@app.route('/search')
def search():
    author = request.args.get("author")
    return list(map(book_structure, Book.search(author)))

if __name__ == "__main__":
    app.run()
    