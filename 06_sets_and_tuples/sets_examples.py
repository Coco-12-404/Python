"""Sets: unordered collections of unique items."""

# --- Example 1: creating sets and uniqueness ---
numbers = {1, 2, 2, 3, 3, 3}
print("Example 1:", numbers)                  # duplicates disappear
empty_set = set()                             # {} would create a dict!
print(type({}), type(empty_set))

# --- Example 2: removing duplicates from a list ---
names = ["Ana", "Ben", "Ana", "Cara", "Ben"]
unique_names = list(set(names))               # order is not guaranteed
print("\nExample 2:", sorted(unique_names))

# --- Example 3: adding and removing ---
tags = {"python", "code"}
tags.add("learn")
tags.add("python")            # already there - no change
tags.discard("missing")       # safe: no error if absent
tags.remove("code")           # raises KeyError if absent
print("\nExample 3:", sorted(tags))

# --- Example 4: set operations ---
class_a = {"Ana", "Ben", "Cara"}
class_b = {"Cara", "Dev", "Eli"}
print("\nExample 4:")
print("Both:", class_a & class_b)              # intersection
print("Either:", sorted(class_a | class_b))    # union
print("Only A:", class_a - class_b)            # difference
print("In one only:", sorted(class_a ^ class_b))  # symmetric difference

# --- Example 5: fast membership tests and subsets ---
print("\nExample 5:")
print("Ana" in class_a)
print({"Ana", "Ben"}.issubset(class_a))

# --- Example 6: practical - find new visitors ---
yesterday = {"u1", "u2", "u3"}
today = {"u2", "u3", "u4", "u5"}
print("\nExample 6: new visitors:", sorted(today - yesterday))

# --- Common mistakes ---
print("\nCommon mistakes:")
try:
    print(numbers[0])                 # sets have no order/index
except TypeError as error:
    print("  TypeError:", error)

try:
    tags.remove("nothing")
except KeyError as error:
    print("  KeyError:", error)

try:
    bad_set = {[1, 2], [3]}           # lists are unhashable
except TypeError as error:
    print("  TypeError:", error)
