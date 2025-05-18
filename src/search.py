# search.py

from book import BookManager, Book
from typing import List, Optional


def search_by_title(manager: BookManager, title: str) -> List[Book]:
    """
    Search books by title.
    
    Args:
        manager (BookManager): The book manager instance.
        title (str): The title or part of title to search.

    Returns:
        List[Book]: List of matching Book objects.
    """
    matches = [
        book for book in manager.books.values()
        if title.lower() in book.title.lower()
    ]
    return matches


def search_by_author(manager: BookManager, author: str) -> List[Book]:
    """
    Search books by author.

    Args:
        manager (BookManager): The book manager instance.
        author (str): The author or part of author name to search.

    Returns:
        List[Book]: List of matching Book objects.
    """
    matches = [
        book for book in manager.books.values()
        if author.lower() in book.author.lower()
    ]
    return matches


def search_by_isbn(manager: BookManager, isbn: str) -> Optional[Book]:
    """
    Search book by ISBN.

    Args:
        manager (BookManager): The book manager instance.
        isbn (str): ISBN to search for.

    Returns:
        Book if found, else None.
    """
    return manager.books.get(isbn)
