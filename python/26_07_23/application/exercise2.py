'''
Create a class Book. Each book object should have the attributes: 
- title
- author (default unknown) 
- number of pages
- genre
- ISBN. 
The class should define the following methods:
- __init__ to set the attributes described above
- __str__ to print a description of the book
- a search method which returns all books by a given author (requires tracking of objects) - if there are no books by the given author return an empty list
- a method to check the validity of a given ISBN-13 - should return true if the ISBN is valid, false otherwise
As an additional stretch goal, create 2 subclasses for specific 
genres and override the __init__ method and __str__ methods appropriately
'''
from typing import List
class Book():
    def __init__(self, title, pages, isbn, genre, author = "Unknown"):
        self.title = title
        self.pages = pages
        self.isbn = isbn
        self.genre = genre
        self.author = author
        Book.books.append(self)
    @property
    def json(self):
        return dict(
            author=self.author,
            title=self.title,
            pages=self.pages,
            isbn=self.isbn
        )
    
    @staticmethod
    def valid_isbn(isbn):
       digits = ''.join(isbn.split('-'))
       if len(digits) !=13:
           return False
       digilist = [int(digit) for digit in digits]
       return ((sum([digits[i] for i in range(12) if i % 2 ==0]) + 3 * sum([digilist[i] for i in range(12) if i % 2 != 0]) + digilist[-1]) % 10) == 0
    
    
    @staticmethod
    def search(author):
        return list(filter(lambda book: book.author == author, Book.books))
        

    def __str__(self):
        return f"Written by {self.author}, {self.title} is a gripping {self.pages}-page"

class BookList:
    def __init__(self, *args):
        self._books = list(args)

    def get(self, book_id) -> Book:
        return self.filter(id=book_id)[0]

    def create(self, *args, **kwargs) -> Book:
        book = Book(*args, **kwargs)
        self._books.append(book)
        self.update_ids()
        return book

    def filter(self, **kwargs) -> List[Book]:
        valid = list(self._books)

        for key, value in kwargs.items():
            valid = [book for book in valid if getattr(book, key) == value]

        return valid