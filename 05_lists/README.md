# 05 - Lists

A **list** is an ordered, changeable collection: `items = [1, "two", 3.0]`.

## Key points
- Indexing starts at 0; negative indexes count from the end (`items[-1]`).
- Slicing: `items[start:stop:step]` (stop is excluded).
- Add: `append`, `insert`, `extend`. Remove: `remove`, `pop`, `del`.
- `sort()` changes the list and returns `None`; `sorted()` returns a new list.
- `b = a` does **not** copy; use `a.copy()` or `a[:]`.
- List comprehensions: `[n * n for n in range(5)]`.
- Common errors: `IndexError` (bad index), `ValueError` (`remove` of a missing item).

## Run
```
python examples.py
python exercises.py
```
