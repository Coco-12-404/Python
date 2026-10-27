# 08 - Operators

| Kind | Operators |
|------|-----------|
| Arithmetic | `+  -  *  /  //  %  **` |
| Assignment | `=  +=  -=  *=  /=  //=  %=  **=` |
| Comparison | `==  !=  <  >  <=  >=` |
| Logical | `and  or  not` |
| Membership | `in  not in` |
| Identity | `is  is not` |

## Key points
- `/` always gives a float; `//` floors the result; `%` gives the remainder.
- Precedence (high to low): `()`, `**`, unary `-`, `* / // %`, `+ -`, comparisons, `not`, `and`, `or`. Use parentheses when unsure.
- `+` and `*` also work on strings and lists.
- `divmod(a, b)` returns `(a // b, a % b)`.
- Pitfalls: `ZeroDivisionError`, mixing `str` and `int`, float rounding (`0.1 + 0.2`).

## Run
```
python examples.py
python exercises.py
```
