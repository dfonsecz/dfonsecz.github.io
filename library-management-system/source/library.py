import json
from datetime import datetime, timedelta
from book import Book
from user import User

class Library:
    """
    Manages the library's book and user data.
    Provides methods to borrow, return, add, remove, and search books.
    """

    def __init__(self):
        """
        Initializes the Library and loads data from files.
        """
        self.books = self.load_books()
        self.users = self.load_users()

    def load_books(self):
        """
        Loads books from 'books.json'.

        Returns:
            dict: Dictionary of Book objects keyed by ISBN.
        """
        try:
            with open('data/books.json', 'r') as f:
                return {b["isbn"]: Book.from_dict(b) for b in json.load(f)}
        except FileNotFoundError:
            return {}

    def save_books(self):
        """
        Saves all books to 'books.json'.
        """
        with open('data/books.json', 'w') as f:
            json.dump([b.to_dict() for b in self.books.values()], f, indent=2)

    def load_users(self):
        """
        Loads users from 'users.json'.

        Returns:
            dict: Dictionary of User objects keyed by user ID.
        """
        try:
            with open('data/users.json', 'r') as f:
                return {u["user_id"]: User.from_dict(u) for u in json.load(f)}
        except FileNotFoundError:
            return {}

    def save_users(self):
        """
        Saves all users to 'users.json'.
        """
        with open('data/users.json', 'w') as f:
            json.dump([u.to_dict() for u in self.users.values()], f, indent=2)

    def add_book(self, book):
        """
        Adds a new book to the system.

        Args:
            book (Book): The book to add.
        """
        self.books[book.isbn] = book
        self.save_books()

    def remove_book(self, isbn):
        """
        Removes a book from the system.

        Args:
            isbn (str): ISBN of the book to remove.
        """
        if isbn in self.books:
            del self.books[isbn]
            self.save_books()

    def add_user(self, user):
        """
        Adds a new user to the system.

        Args:
            user (User): The user to add.
        """
        self.users[user.user_id] = user
        self.save_users()

    def borrow_book(self, user_id, isbn, days=14):
        """
        Borrows a book for a user.

        Args:
            user_id (str): ID of the user borrowing the book.
            isbn (str): ISBN of the book.
            days (int): Number of days until the due date.

        Returns:
            bool: True if borrowing succeeded, False otherwise.
        """
        if isbn in self.books and user_id in self.users:
            book = self.books[isbn]
            if not book.is_borrowed:
                due_date = (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")
                book.mark_as_borrowed(user_id, due_date)
                self.save_books()
                return True
        return False

    def return_book(self, isbn):
        """
        Returns a borrowed book.

        Args:
            isbn (str): ISBN of the book.

        Returns:
            bool: True if return succeeded, False otherwise.
        """
        if isbn in self.books:
            book = self.books[isbn]
            if book.is_borrowed:
                book.mark_as_returned()
                self.save_books()
                return True
        return False

    def search_books(self, title=None, author=None, isbn=None):
        """
        Searches for books based on title, author, or ISBN.

        Returns:
            list: List of matching Book objects.
        """
        results = list(self.books.values())
        if title:
            results = [b for b in results if title.lower() in b.title.lower()]
        if author:
            results = [b for b in results if author.lower() in b.author.lower()]
        if isbn:
            results = [b for b in results if isbn == b.isbn]
        return results

    def get_overdue_books(self):
        """
        Retrieves a list of all overdue books.

        Returns:
            list: List of overdue Book objects.
        """
        today = datetime.now().strftime("%Y-%m-%d")
        return [b for b in self.books.values() if b.is_borrowed and b.due_date < today]
