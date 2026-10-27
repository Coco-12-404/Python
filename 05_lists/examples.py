"""Lists: ordered, changeable collections."""

# --- Example 1: creating and accessing ---
fruits = ["apple", "banana", "cherry"]
print("Example 1:", fruits)
print(fruits[0], fruits[-1])       # first and last
print(len(fruits))

# --- Example 2: slicing ---
numbers = [10, 20, 30, 40, 50]
print("\nExample 2:")
print(numbers[1:4])    # [20, 30, 40]  (end index is excluded)
print(numbers[:2])     # first two
print(numbers[::-1])   # reversed copy
print(numbers[::2])    # every second item

# --- Example 3: adding items ---
todo = ["study"]
todo.append("exercise")        # add to end
todo.insert(0, "wake up")      # add at a position
todo.extend(["cook", "sleep"]) # add several
print("\nExample 3:", todo)

# --- Example 4: removing items ---
todo.remove("cook")            # by value
last = todo.pop()              # remove and return last
del todo[0]                    # by index
print("\nExample 4:", todo, "| popped:", last)

# --- Example 5: sorting ---
scores = [78, 92, 65, 88]
print("\nExample 5:")
print(sorted(scores))                  # new sorted list, original unchanged
scores.sort(reverse=True)              # sorts in place
print(scores)
print("max/min/sum:", max(scores), min(scores), sum(scores))

# --- Example 6: searching ---
print("\nExample 6:")
print("banana" in fruits)              # True
print(fruits.index("cherry"))          # 2
print([1, 2, 2, 3, 2].count(2))        # 3

# --- Example 7: looping and list comprehension ---
print("\nExample 7:")
for position, fruit in enumerate(fruits, start=1):
    print(f"{position}. {fruit}")
squares = [n * n for n in range(1, 6)]     # compact way to build a list
print(squares)
print([n for n in numbers if n > 25])      # filtering

# --- Example 8: practical - average of marks ---
marks = [72, 85, 90, 64]
print(f"\nExample 8: average = {sum(marks) / len(marks):.1f}")

# --- Example 9: nested lists ---
grid = [[1, 2, 3], [4, 5, 6]]
print("\nExample 9:", grid[1][2])   # row 1, column 2 -> 6

# --- Common mistakes ---
print("\nCommon mistakes:")
try:
    print(fruits[10])                 # beyond the end
except IndexError as error:
    print("  IndexError:", error)

try:
    fruits.remove("mango")            # not in the list
except ValueError as error:
    print("  ValueError:", error)

alias = fruits                         # NOT a copy - same list
alias.append("grape")
print("  alias changed the original too:", fruits)
real_copy = fruits.copy()              # use copy() or fruits[:]
real_copy.append("kiwi")
print("  copy is separate:", fruits, "vs", real_copy)

result = [3, 1, 2].sort()              # sort() returns None!
print("  sort() returns:", result)
