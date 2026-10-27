# Python Learning Progress

This repository tracks my journey of learning Python. Each topic has runnable
examples, practice exercises, and a short explanation. It uses only Python's
standard library - no extra packages needed.

## Topics

| # | Topic | What it covers |
|---|-------|----------------|
| 01 | [Variables](01_variables/) | Naming, types, reassignment, type conversion |
| 02 | [Comments](02_comments/) | `#` comments, docstrings, good commenting habits |
| 03 | [String formatting](03_string_formatting/) | f-strings, `.format()`, `%`, alignment, string methods |
| 04 | [User input](04_user_input/) | `input()`, converting types, validating input |
| 05 | [Lists](05_lists/) | Indexing, slicing, add/remove, sorting, comprehensions |
| 06 | [Sets and tuples](06_sets_and_tuples/) | Unique items, set maths, immutable tuples, unpacking |
| 07 | [Booleans](07_booleans/) | `True`/`False`, comparisons, `and`/`or`/`not`, truthiness |
| 08 | [Operators](08_operators/) | Arithmetic, assignment, comparison, membership, precedence |
| 09 | [Conditional statements](09_conditional_statements/) | `if` / `elif` / `else`, nesting, ternary |
| 10 | [Loops](10_loops/) | `for`, `while`, `range`, `break`, `continue`, nested loops |
| 11 | [Dictionaries](11_dictionaries/) | Key-value pairs, looping, counting, nesting |
| 12 | [Functions](12_functions/) | Parameters, return values, defaults, keyword arguments |
| 13 | [Object-oriented programming](13_object_oriented_programming/) | Classes, objects, `__init__`, properties, inheritance, polymorphism, abstraction, composition, dunder methods, mini-project *(in progress)* |

Each folder contains `examples.py` (or similarly named example files), `exercises.py`, and a `README.md`.

## Setup

1. Install Python 3.10 or newer from <https://www.python.org/downloads/>.
2. Check the install:
   ```
   python --version
   ```
   (On macOS/Linux you may need `python3`.)
3. Clone and enter the repository:
   ```
   git clone https://github.com/Coco-12-404/Python.git
   cd Python
   ```
4. A virtual environment is optional because there are no dependencies:
   ```
   python -m venv .venv
   ```

## Running programs

From the repository root:

```
python 01_variables/examples.py
python 05_lists/examples.py
python 10_loops/for_loops.py
```

Or move into a folder first:

```
cd 12_functions
python examples.py
python exercises.py
```

Files that ask for input (`04_user_input/examples.py`, `10_loops/interactive_loop.py`,
`09_conditional_statements/interactive_example.py`, `12_functions/interactive_example.py`)
wait for you to type. Press `Ctrl+C` to stop any running program.

To check the input helpers without typing anything:

```
python 04_user_input/test_helpers.py
```

## How to practise

1. Read the topic's `README.md`.
2. Run the examples and change values to see what happens.
3. Open `exercises.py`, replace each `# TODO` with your own solution, and run it.
4. Tick the exercises checkbox below when you have solved them yourself.

## Progress checklist

Topics learned (studied):

- [x] 01 Variables
- [x] 02 Comments
- [x] 03 String formatting
- [x] 04 Getting user input
- [x] 05 Lists
- [x] 06 Sets and tuples
- [x] 07 Booleans
- [x] 08 Operators
- [x] 09 Conditional statements
- [x] 10 Loops
- [x] 11 Dictionaries
- [x] 12 Functions
- [ ] 13 Object-oriented programming (in progress)

Exercises completed:

- [ ] 01 Variables exercises
- [ ] 02 Comments exercises
- [ ] 03 String formatting exercises
- [ ] 04 User input exercises
- [ ] 05 Lists exercises
- [ ] 06 Sets and tuples exercises
- [ ] 07 Booleans exercises
- [ ] 08 Operators exercises
- [ ] 09 Conditional statements exercises
- [ ] 10 Loops exercises
- [ ] 11 Dictionaries exercises
- [ ] 12 Functions exercises
- [ ] 13 Object-oriented programming exercises

## Future topics

Add a new numbered folder (for example `14_file_handling/`) with the same three
files, then add it to the table and checklist above.

- [ ] Error handling (`try` / `except`) in depth
- [ ] File handling
- [ ] Modules and imports
- [ ] Classes and objects
- [ ] Comprehensions in depth
- [ ] Recursion
- [ ] Testing
