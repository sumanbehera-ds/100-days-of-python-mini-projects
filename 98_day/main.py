# Library Book Management System
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def borrow_book(self):
        if self.copies <= 0:
            print("Book not available")
            return False
        self.copies -= 1
        print("Book borrowed successfully")
        return True

    def return_book(self):
        self.copies += 1
        print("Book returned successfully")

    def display_book(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Available Copies:", self.copies)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            book.display_book()
            print("-" * 20)


library = Library()
book1 = Book("Python Basics", "John Smith", 3)
book2 = Book("Machine Learning", "Andrew Ng", 2)

library.add_book(book1)
library.add_book(book2)
library.show_books()
book1.borrow_book()
library.show_books()