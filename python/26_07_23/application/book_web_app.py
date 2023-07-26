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

books = BookList(
    Book("John Johnson", "Book Title", "200", "1235433865"),
    Book("Dorothy", "The wonderful world of os", "67", "904757363")
)

books.update_ids()

def get_args():
    return {key: value for key, value in request.args.items() if key in ("title", "author", "pages", "isbn")}

@app.route("/")


def index():
    return [book.json for book in books.filter(**get_args())]

@app.route('/create')
def create():
    try:
        book = books.create(**get_args())
        return book.json

    except TypeError as err:
        return str(err)


@app.route('/<int:book_id>')
def get(book_id):
    return books.get(book_id).json

if __name__ == "__main__":
    app.run()
    