"""Interactive command-line Library Management System.

Run: python main.py
"""

from library import Library

MENU = """
=== Library Menu ===
1. Add book
2. Register member
3. Borrow book
4. Return book
5. List all books
6. List available books
7. Search books
8. List members
q. Quit"""


def show_books(books):
    if not books:
        print("  (none)")
    for book in books:
        print("  ", book)


def run(library):
    while True:
        print(MENU)
        choice = input("Choose: ").strip().lower()
        try:
            if choice == "1":
                book = library.add_book(input("ISBN: "), input("Title: "), input("Author: "))
                print("  Added:", book)
            elif choice == "2":
                member = library.register_member(input("Member ID: "), input("Name: "))
                print("  Registered:", member)
            elif choice == "3":
                print("  ", library.borrow_book(input("Member ID: ").strip(), input("ISBN: ").strip()))
            elif choice == "4":
                print("  ", library.return_book(input("Member ID: ").strip(), input("ISBN: ").strip()))
            elif choice == "5":
                show_books(library.books)
            elif choice == "6":
                show_books(library.available_books())
            elif choice == "7":
                show_books(library.search(input("Search text: ")))
            elif choice == "8":
                for member in library.members:
                    print("  ", member)
                if not library.members:
                    print("  (none)")
            elif choice == "q":
                print("Goodbye!")
                return
            else:
                print("  Invalid choice, try again.")
        except ValueError as error:           # every rule violation lands here
            print("  Error:", error)


def main():
    library = Library("City Library")
    library.add_book("111", "Python Basics", "Asha Rao")      # sample data
    library.add_book("222", "Data Structures", "Ravi Iyer")
    library.register_member("M1", "Dev")
    print("Sample data loaded: books 111, 222 and member M1.")
    run(library)


if __name__ == "__main__":
    main()
