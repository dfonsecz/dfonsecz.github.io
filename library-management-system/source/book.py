from datetime import datetime

class Book:
    """
    Represents a book in the library.
    
    Attributes:
        title (str): The title of the book.
        author (str): The author's name.
        isbn (str): The unique ISBN identifier.
        is_borrowed (bool): True if the book is currently borrowed.
        due_date (str): The due date as a string (YYYY-MM-DD), or None.
        borrower_id (str): ID of the user who borrowed the book.
    """

    def __init__(self, title, author, isbn):
        """
        Initializes a new Book object.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.due_date = None
        self.borrower_id = None

    def mark_as_borrowed(self, borrower_id, due_date):
        """
        Marks the book as borrowed.
        
        Args:
            borrower_id (str): The ID of the borrower.
            due_date (str): Due date in YYYY-MM-DD format.
        """
        self.is_borrowed = True
        self.due_date = due_date
        self.borrower_id = borrower_id

    def mark_as_returned(self):
        """
        Marks the book as returned.
        """
        self.is_borrowed = False
        self.due_date = None
        self.borrower_id = None

    def to_dict(self):
        """
        Converts the Book object to a dictionary.
        
        Returns:
            dict: Dictionary representation of the book.
        """
        return self.__dict__

    @staticmethod
    def from_dict(data):
        """
        Creates a Book object from a dictionary.
        
        Args:
            data (dict): Dictionary with book data.
        
        Returns:
            Book: A new Book instance.
        """
        book = Book(data["title"], data["author"], data["isbn"])
        book.is_borrowed = data["is_borrowed"]
        book.due_date = data["due_date"]
        book.borrower_id = data["borrower_id"]
        return book
