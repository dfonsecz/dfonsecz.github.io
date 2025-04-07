from library import Library
from book import Book
from user import User

lib = Library()

def main_menu():
    """
    """
    print("\n=== Library System ===")
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Search Books")
    print("5. List Overdue Books")
    print("0. Exit")

while True:
    main_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        lib.add_book(Book(title, author, isbn))
        print("Book added!")

    elif choice == "2":
        user_id = input("User ID: ")
        if user_id not in lib.users:
            name = input("Name: ")
            lib.add_user(User(name, user_id))
        isbn = input("ISBN of book to borrow: ")
        if lib.borrow_book(user_id, isbn):
            print("Book borrowed!")
        else:
            print("Failed to borrow book.")

    elif choice == "3":
        isbn = input("ISBN of book to return: ")
        if lib.return_book(isbn):
            print("Book returned!")
        else:
            print("Failed to return book.")

    elif choice == "4":
        term = input("Search by title/author/ISBN: ")
        results = lib.search_books(title=term) + lib.search_books(author=term) + lib.search_books(isbn=term)
        found = {b.isbn: b for b in results}.values()
        for book in found:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{book.title} by {book.author} [{book.isbn}] - {status}")

    elif choice == "5":
        overdue = lib.get_overdue_books()
        if overdue:
            print("Overdue Books:")
            for b in overdue:
                print(f"{b.title} (Due: {b.due_date})")
        else:
            print("No overdue books.")

    elif choice == "0":
        break
