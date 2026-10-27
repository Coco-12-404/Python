# 02 - Comments

Comments are notes for humans. Python ignores them.

```python
# single-line comment
x = 5  # inline comment

def square(n):
    """Docstring: describes the function."""
    return n * n
```

## Key points
- `#` starts a comment that lasts until the end of the line.
- Explain **why**, not the obvious **what**.
- Docstrings (`"""..."""`) document files and functions; see them with `.__doc__`.
- Comment out code temporarily while debugging.
- A `#` inside a string is just text.
- Keep comments up to date.

## Run
```
python examples.py
python exercises.py
```
