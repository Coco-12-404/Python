# 11 - Dictionaries

A **dictionary** stores `key: value` pairs and looks values up by key.

```python
student = {"name": "Asha", "age": 21}
student["city"] = "Pune"        # add / update
print(student.get("email", "none"))
for key, value in student.items():
    print(key, value)
```

## Key points
- Keys are unique and must be hashable (strings, numbers, tuples - not lists).
- `d[key]` raises `KeyError` if missing; `d.get(key, default)` does not.
- Remove: `pop(key)`, `del d[key]`. Check keys with `key in d`.
- Loop with `.keys()`, `.values()`, `.items()`.
- Handy patterns: counting (`d[k] = d.get(k, 0) + 1`), grouping (`setdefault`), nesting, merging (`{**a, **b}`).
- `b = a` is not a copy; use `a.copy()`.

## Run
```
python examples.py
python exercises.py
```
