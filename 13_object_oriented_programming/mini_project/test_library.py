"""Lightweight tests for the mini-project (standard library only).

Run: python test_library.py
"""

import unittest

from book import Book
from library import Library
from member import Member


class LibraryTests(unittest.TestCase):
    def setUp(self):
        self.library = Library("Test")
        for isbn, title in (("1", "A"), ("2", "B"), ("3", "C"), ("4", "D")):
            self.library.add_book(isbn, title, "Author")
        self.library.register_member("M1", "Dev")
        self.library.register_member("M2", "Anu")

    def test_borrow_and_return(self):
        self.library.borrow_book("M1", "1")
        self.assertFalse(self.library.get_book("1").is_available)
        self.assertEqual(len(self.library.get_member("M1")), 1)
        self.library.return_book("M1", "1")
        self.assertTrue(self.library.get_book("1").is_available)
        self.assertEqual(len(self.library.get_member("M1")), 0)

    def test_unavailable_book(self):
        self.library.borrow_book("M1", "1")
        with self.assertRaises(ValueError):
            self.library.borrow_book("M2", "1")
        self.assertEqual(len(self.library.get_member("M2")), 0)   # no partial change

    def test_borrow_limit(self):
        for isbn in ("1", "2", "3"):
            self.library.borrow_book("M1", isbn)
        with self.assertRaises(ValueError):
            self.library.borrow_book("M1", "4")
        self.assertTrue(self.library.get_book("4").is_available)

    def test_invalid_operations(self):
        with self.assertRaises(ValueError):
            self.library.borrow_book("nobody", "1")
        with self.assertRaises(ValueError):
            self.library.borrow_book("M1", "999")
        with self.assertRaises(ValueError):
            self.library.return_book("M1", "1")           # not borrowed
        self.library.borrow_book("M1", "1")
        with self.assertRaises(ValueError):
            self.library.return_book("M2", "1")           # borrowed by someone else
        with self.assertRaises(ValueError):
            self.library.add_book("1", "Dup", "X")
        with self.assertRaises(ValueError):
            self.library.register_member("M1", "Dup")
        with self.assertRaises(ValueError):
            Book("", "T", "A")
        with self.assertRaises(ValueError):
            Member("M3", "  ")

    def test_special_methods(self):
        self.assertEqual(len(self.library), 4)
        self.assertIn("available", str(self.library.get_book("1")))
        self.assertIn("Book(", repr(self.library.get_book("1")))
        self.assertEqual(Book("1", "x", "y"), Book("1", "z", "w"))

    def test_search_and_availability(self):
        self.library.borrow_book("M1", "1")
        self.assertEqual(len(self.library.available_books()), 3)
        self.assertEqual(len(self.library.search("author")), 4)

    def test_encapsulation_copy(self):
        self.library.borrow_book("M1", "1")
        self.library.get_member("M1").borrowed_isbns.append("junk")   # edits a copy
        self.assertEqual(self.library.get_member("M1").borrowed_isbns, ["1"])


if __name__ == "__main__":
    unittest.main()
