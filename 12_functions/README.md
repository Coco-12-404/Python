# 12 - Functions

A **function** is a named, reusable block of code.

```python
def greet_user(name, greeting="Hello"):
    """Return a greeting message."""
    return f"{greeting}, {name}!"

print(greet_user("Asha"))
print(greet_user(greeting="Hi", name="Ravi"))   # keyword arguments
```

## Key points
- `def name(parameters):` defines it; call it with `name(arguments)`.
- `return` sends a value back; without it a function returns `None`. Printing is not returning.
- Default arguments make parameters optional; keyword arguments let you pass them by name.
- Return several values as a tuple and unpack them.
- Variables created inside a function are local to it.
- Never use a mutable default (`items=[]`); use `None` and create the list inside.
- Optional: `*args` accepts any number of positional arguments.
- Add a docstring to describe what the function does.

## Files
- `examples.py` - non-interactive examples
- `interactive_example.py` - unit-converter menu with `input()`
- `exercises.py` - practice

## Run
```
python examples.py
python interactive_example.py
python exercises.py
```
