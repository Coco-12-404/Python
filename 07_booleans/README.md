# 07 - Booleans

A `bool` is either `True` or `False`. Comparisons produce booleans.

```python
age = 20
print(age > 18)                  # True
print(age > 18 and age < 65)     # True
print(not (age > 18))            # False
```

## Key points
- Comparison operators: `==  !=  <  >  <=  >=`; chaining works: `1 < x < 10`.
- Logic operators: `and`, `or`, `not`. `and`/`or` short-circuit.
- **Falsy** values: `0`, `0.0`, `""`, `[]`, `()`, `{}`, `set()`, `None`, `False`. Most others are truthy.
- `in`, `not in`, `is`, `is not` also return booleans. Use `is None` for `None`.
- Pitfalls: `=` assigns, `==` compares; `bool("False")` is `True`; floats can be inexact (`0.1 + 0.2 != 0.3`).

## Run
```
python examples.py
python exercises.py
```
