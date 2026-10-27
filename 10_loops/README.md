# 10 - Loops

## `for` - iterate over a sequence
```python
for number in range(1, 4):
    print(number)
```

## `while` - repeat while a condition is true
```python
count = 3
while count > 0:
    print(count)
    count -= 1
```

## Key points
- `range(stop)`, `range(start, stop)`, `range(start, stop, step)` - `stop` is excluded.
- `enumerate()` gives index and value; `zip()` walks two lists together.
- `break` exits the loop, `continue` skips to the next round; loop `else` runs if no `break` happened.
- A `while` loop must change something so the condition eventually becomes false (otherwise it is infinite; press Ctrl+C to stop).
- Do not remove items from a list while looping over it; loop over a copy.

## Files
- `for_loops.py` - `for` examples
- `while_loops.py` - `while` examples
- `interactive_loop.py` - guessing game and running total (uses `input()`)
- `exercises.py` - practice

## Run
```
python for_loops.py
python while_loops.py
python interactive_loop.py
python exercises.py
```
