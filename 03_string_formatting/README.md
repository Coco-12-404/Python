# 03 - String Formatting

Ways to insert values into text.

```python
name, price = "Asha", 1234.5678
print(f"{name} paid {price:,.2f}")          # f-string (preferred)
print("{} paid {:.2f}".format(name, price)) # str.format()
print("%s paid %.2f" % (name, price))       # old style
```

## Key points
- f-strings need the `f` prefix and can hold expressions: `f"{a + b}"`.
- Format specs: `:.2f` decimals, `:,` thousands, `:>10` right-align, `:<10` left, `:^10` center, `:03d` zero-pad, `:.1%` percent.
- `.format()` supports positions (`{0}`) and names (`{n}`).
- Useful methods: `strip`, `lower`, `upper`, `title`, `replace`, `split`, `join`.
- Literal braces in f-strings: `{{` and `}}`.
- Concatenating `str + int` raises `TypeError`.

## Run
```
python examples.py
python exercises.py
```
