"""Member class: a person who can borrow books."""


class Member:
    """A library member with a limit on how many books they can hold."""

    MAX_BOOKS = 3                          # class attribute shared by all members

    def __init__(self, member_id, name):
        if not member_id.strip() or not name.strip():
            raise ValueError("Member ID and name are required")
        self.member_id = member_id.strip()
        self.name = name.strip()
        self._borrowed_isbns = []          # ISBNs only: the Library owns the Books

    @property
    def borrowed_isbns(self):
        return list(self._borrowed_isbns)  # return a copy so outsiders can't edit it

    def can_borrow(self):
        return len(self._borrowed_isbns) < self.MAX_BOOKS

    def add_loan(self, isbn):
        if not self.can_borrow():
            raise ValueError(f"{self.name} has reached the limit of {self.MAX_BOOKS} books")
        self._borrowed_isbns.append(isbn)

    def remove_loan(self, isbn):
        if isbn not in self._borrowed_isbns:
            raise ValueError(f"{self.name} has not borrowed book {isbn}")
        self._borrowed_isbns.remove(isbn)

    def __len__(self):
        return len(self._borrowed_isbns)   # len(member) = books currently held

    def __str__(self):
        return f"{self.name} ({self.member_id}) - {len(self)} book(s) borrowed"

    def __repr__(self):
        return f"Member(member_id={self.member_id!r}, name={self.name!r})"
