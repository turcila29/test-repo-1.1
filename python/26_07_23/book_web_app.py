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
app = Flask(__name__)

@app.route("/")


def index():
    return("Welcome to the library")

@app.route('/books')

def addbooks():
    pass

if __name__ == "__main__":
    app.run()
    