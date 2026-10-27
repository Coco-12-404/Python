# Mini-Project: Library Management System

A command-line library built with OOP. No databases or external packages.

## Files
| File | Purpose |
|------|---------|
| `book.py` | `Book` - one title; tracks who borrowed it |
| `member.py` | `Member` - a person; limited to 3 books |
| `library.py` | `Library` - owns books and members, enforces the rules |
| `main.py` | Interactive menu |
| `demo.py` | Non-interactive walkthrough with sample output |
| `test_library.py` | Automated tests (`unittest`) |

## Design
- **Composition:** a `Library` *has* books and members (stored in dictionaries keyed by ISBN / member ID).
- **Constructors + validation:** `Book` and `Member` reject empty values.
- **Encapsulation:** `Book._borrowed_by` and `Member._borrowed_isbns` are changed only through methods; `borrowed_isbns` returns a copy.
- **Properties:** `Book.is_available`, `Book.borrowed_by`.
- **Class attribute:** `Member.MAX_BOOKS = 3`.
- **Special methods:** `__str__`, `__repr__`, `__eq__`, `__hash__` (Book); `__len__` (Member, Library).
- **Error handling:** rule violations raise `ValueError` with a clear message; `main.py` catches them and prints the message.
- `Library.borrow_book` checks every rule *before* changing anything, so a failed borrow leaves no half-done state.

## Run
From the repository root:
```
python 13_object_oriented_programming/mini_project/demo.py
python 13_object_oriented_programming/mini_project/main.py
python 13_object_oriented_programming/mini_project/test_library.py
```
Or from inside this folder: `python demo.py`, `python main.py`, `python test_library.py`.

## Ideas to extend (optional)
- Due dates using `datetime`
- A `Librarian` subclass of `Member`
- Saving data to a JSON file
