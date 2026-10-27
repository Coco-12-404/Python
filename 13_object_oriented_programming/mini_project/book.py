"""Book class: one title in the library."""


class Book:
    """A book that can be borrowed by one member at a time."""

    def __init__(self, isbn, title, author):
        if not isbn.strip() or not title.strip() or not author.strip():
            raise ValueError("ISBN, title and author are all required")
        self.isbn = isbn.strip()
        self.title = title.strip()
        self.author = author.strip()
        self._borrowed_by = None          # protected: change via borrow()/give_back()

    @property
    def is_available(self):
        return self._borrowed_by is None

    @property
    def borrowed_by(self):
        return self._borrowed_by

    def borrow(self, member_id):
        if not self.is_available:
            raise ValueError(f"'{self.title}' is already borrowed by member {self._borrowed_by}")
        self._borrowed_by = member_id

    def give_back(self):
        if self.is_available:
            raise ValueError(f"'{self.title}' was not borrowed")
        self._borrowed_by = None

    def __str__(self):
        status = "available" if self.is_available else f"borrowed by {self._borrowed_by}"
        return f"[{self.isbn}] {self.title} by {self.author} ({status})"

    def __repr__(self):
        return f"Book(isbn={self.isbn!r}, title={self.title!r}, author={self.author!r})"

    def __eq__(self, other):
        return isinstance(other, Book) and self.isbn == other.isbn

    def __hash__(self):
        return hash(self.isbn)
