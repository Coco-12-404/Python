# 04 - Getting User Input

`input(prompt)` pauses the program, reads a line, and returns it as a **string**.

```python
name = input("Name: ")
age = int(input("Age: "))       # convert to a number when needed
```

## Key points
- Always a `str` - convert with `int()` / `float()` for maths.
- Invalid text like `"abc"` raises `ValueError`; handle it with `try/except` in a `while` loop.
- `.strip()` removes stray spaces, `.lower()` makes comparisons easier.
- `.split()` turns one line into several values.
- `examples.py` has reusable helpers (`ask_int`, `ask_float`, `ask_yes_no`); `test_helpers.py` checks them without typing anything.

## Run
```
python examples.py        # interactive
python test_helpers.py    # automatic check, no typing
python exercises.py
```
