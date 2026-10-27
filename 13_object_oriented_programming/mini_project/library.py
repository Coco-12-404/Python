"""Library class: owns books and members (composition) and coordinates loans."""

from book import Book
from member import Member


class Library:
    """A library HAS books and members. Methods return a message for the user
    and raise ValueError for invalid operations (callers decide how to show it)."""

    def __init__(self, name):
        self.name = name
        self._books = {}       # isbn -> Book
        self._members = {}     # member_id -> Member

    # --- adding things ---
    def add_book(self, isbn, title, author):
        if isbn.strip() in self._books:
            raise ValueError(f"A book with ISBN {isbn} already exists")
        book = Book(isbn, title, author)
        self._books[book.isbn] = book
        return book

    def register_member(self, member_id, name):
        if member_id.strip() in self._members:
            raise ValueError(f"Member ID {member_id} is already registered")
        member = Member(member_id, name)
        self._members[member.member_id] = member
        return member

    # --- lookups ---
    def get_book(self, isbn):
        if isbn not in self._books:
            raise ValueError(f"No book with ISBN {isbn}")
        return self._books[isbn]

    def get_member(self, member_id):
        if member_id not in self._members:
            raise ValueError(f"No member with ID {member_id}")
        return self._members[member_id]

    def available_books(self):
        return [book for book in self._books.values() if book.is_available]

    def search(self, text):
        text = text.lower()
        return [b for b in self._books.values()
                if text in b.title.lower() or text in b.author.lower()]

    # --- borrowing and returning ---
    def borrow_book(self, member_id, isbn):
        member = self.get_member(member_id)
        book = self.get_book(isbn)
        if not member.can_borrow():            # check everything BEFORE changing anything
            raise ValueError(f"{member.name} has reached the limit of {Member.MAX_BOOKS} books")
        book.borrow(member.member_id)          # raises if unavailable
        member.add_loan(book.isbn)
        return f"{member.name} borrowed '{book.title}'"

    def return_book(self, member_id, isbn):
        member = self.get_member(member_id)
        book = self.get_book(isbn)
        if book.borrowed_by != member.member_id:
            raise ValueError(f"{member.name} has not borrowed '{book.title}'")
        book.give_back()
        member.remove_loan(book.isbn)
        return f"{member.name} returned '{book.title}'"

    # --- special methods ---
    def __len__(self):
        return len(self._books)

    def __str__(self):
        return (f"{self.name}: {len(self._books)} books "
                f"({len(self.available_books())} available), {len(self._members)} members")

    @property
    def books(self):
        return list(self._books.values())

    @property
    def members(self):
        return list(self._members.values())
