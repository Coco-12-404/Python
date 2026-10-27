"""Non-interactive demo of the Library Management System.

Run: python demo.py
"""

from library import Library


def attempt(action, *args):
    """Run a library action and print the result or the error message."""
    try:
        print("  OK:", action(*args))
    except ValueError as error:
        print("  ERROR:", error)


def main():
    library = Library("City Library")
    library.add_book("111", "Python Basics", "Asha Rao")
    library.add_book("222", "Data Structures", "Ravi Iyer")
    library.add_book("333", "Clean Code", "Robert Martin")
    library.add_book("444", "Algorithms", "Meera Shah")
    library.register_member("M1", "Dev")
    library.register_member("M2", "Anu")
    print(library)

    print("\nBorrow a book:")
    attempt(library.borrow_book, "M1", "111")

    print("\nBorrow the same book as someone else (unavailable):")
    attempt(library.borrow_book, "M2", "111")

    print("\nInvalid operations:")
    attempt(library.borrow_book, "M9", "222")      # unknown member
    attempt(library.borrow_book, "M1", "999")      # unknown book
    attempt(library.return_book, "M2", "222")      # never borrowed
    attempt(library.add_book, "111", "Duplicate", "Nobody")

    print("\nBorrowing limit (3 books per member):")
    attempt(library.borrow_book, "M1", "222")
    attempt(library.borrow_book, "M1", "333")
    attempt(library.borrow_book, "M1", "444")

    print("\nReturn and re-borrow:")
    attempt(library.return_book, "M1", "111")
    attempt(library.borrow_book, "M2", "111")

    print("\nSearch for 'data':")
    for book in library.search("data"):
        print("  ", book)

    print("\nFinal state:")
    print(library)
    for book in library.books:
        print("  ", book)
    for member in library.members:
        print("  ", member)


if __name__ == "__main__":
    main()
