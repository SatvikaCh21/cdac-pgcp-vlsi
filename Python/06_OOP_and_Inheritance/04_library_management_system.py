class Book:
    def __init__(self, title, author, is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: '{book.title}' by {book.author}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_available:
                    book.is_available = False
                    print(f"You have borrowed '{book.title}'.")
                    return
                else:
                    print(f"'{book.title}' is currently unavailable.")
                    return
        print(f"Book '{title}' not found in library.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.is_available = True
                print(f"'{book.title}' has been returned.")
                return
        print(f"Book '{title}' not found in library.")

    def display_available_books(self):
        print("Available books:")
        available = [b for b in self.books if b.is_available]
        if not available:
            print("  No books available right now.")
        for book in available:
            print(f"  - {book.title} by {book.author}")

library = Library()
library.add_book(Book("OOPs", "Paulo Coelho"))
library.add_book(Book("Digital Design", "Morris Mano"))
library.add_book(Book("CMOS VLSI Design", "Weste & Harris"))
library.display_available_books()
library.borrow_book("Digital Design")
library.display_available_books()
library.return_book("Digital Design")
library.display_available_books()
library.borrow_book("Unknown Book")