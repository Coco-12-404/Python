# 09 - Conditional Statements

Run different code depending on a condition.

```python
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
else:
    grade = "C"
```

## Key points
- Indentation (4 spaces) defines the block; the line ends with `:`.
- Only the **first** true branch runs, so order `elif`s carefully.
- Combine conditions with `and` / `or` instead of deep nesting.
- Ternary: `"even" if n % 2 == 0 else "odd"`.
- Empty values (`[]`, `""`, `0`, `None`) are falsy: `if items:`.
- Optional: `match`/`case` (Python 3.10+) for many fixed choices.
- Pitfalls: `=` vs `==`, `x == 1 or 2` (always truthy), forgetting the colon.

## Files
- `examples.py` - non-interactive examples
- `interactive_example.py` - ticket calculator using `input()`
- `exercises.py` - practice

## Run
```
python examples.py
python interactive_example.py
python exercises.py
```
