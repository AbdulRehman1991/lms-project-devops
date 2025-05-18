"""Main Class for Book Management System"""


class Book:
    """Represents a book in the library."""
    def __init__(self, isbn, title, author, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.copies = copies


""" Book Manager Class for managing a collection of books"""


class BookManager:
    def __init__(self):
        self.books = {}  # Dictionary to store books with ISBN as key

    """Adds a new book to the collection."""
    def add_book(self, book):
        if book.isbn in self.books:
            print(f"Book with ISBN {book.isbn} already exists. Updating copies.")
            self.books[book.isbn].copies += book.copies  # Update copies if book exists
        else:
            self.books[book.isbn] = book  # Add new book to collection
            print(f"Book '{book.title}' with isbn {book.isbn} added successfully.")

    """ Removes a book from the collection using its ISBN."""
    def remove_book(self, isbn):
        if isbn in self.books:
            removed_book = self.books.pop(isbn)  # Remove book from collection
            print(f"Book '{removed_book.title}' removed successfully.")
        else:
            print(f"No book found with ISBN {isbn}.")

    """ Lists all books in the collection."""
    def list_books(self):
        if not self.books:  # Check if collection is empty
            print("No books available in the library.")
            return
        else:
            for book in self.books.values():
                print(f"ISBN: {book.isbn}, Title: {book.title}, Author: {book.author}, Copies: {book.copies}")


if __name__ == "__main__":
    manager = BookManager()

    book1 = Book('123', 'Python Basics', 'John Doe', 3)
    book2 = Book('456', 'Advanced Python', 'Jane Smith', 2)

    manager.add_book(book1)
    manager.add_book(book2)

    manager.remove_book('123')

    manager.list_books()
