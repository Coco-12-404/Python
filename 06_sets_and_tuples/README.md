# 06 - Sets and Tuples

## Sets - unique, unordered
```python
unique = {1, 2, 2, 3}        # {1, 2, 3}
empty = set()                # {} creates a dict, not a set
a & b   a | b   a - b   a ^ b   # intersection, union, difference, symmetric difference
```
- No duplicates, no indexing; very fast `in` checks.
- `add`, `discard` (safe), `remove` (KeyError if missing).
- Items must be hashable (no lists inside sets).

## Tuples - ordered, immutable
```python
point = (3, 7)
x, y = point                 # unpacking
single = (5,)                # trailing comma needed
```
- Cannot be changed after creation (`TypeError` on assignment).
- Good for fixed records, multiple return values, and dictionary keys.

## Files
- `sets_examples.py` - set examples
- `tuples_examples.py` - tuple examples
- `exercises.py` - practice

## Run
```
python sets_examples.py
python tuples_examples.py
python exercises.py
```
