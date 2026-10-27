"""Tuples: ordered collections that cannot be changed (immutable)."""

# --- Example 1: creating and accessing ---
point = (3, 7)
colors = ("red", "green", "blue")
print("Example 1:", point, colors[0], colors[-1], len(colors))

# --- Example 2: single-item tuple needs a trailing comma ---
not_a_tuple = (5)
real_tuple = (5,)
print("\nExample 2:", type(not_a_tuple), type(real_tuple))

# --- Example 3: unpacking ---
x, y = point
print("\nExample 3: x =", x, "y =", y)
first, *rest = (10, 20, 30, 40)       # optional: * collects the remainder
print(first, rest)

# --- Example 4: returning several values from a function ---
def min_and_max(values):
    return min(values), max(values)    # returns a tuple

lowest, highest = min_and_max([4, 9, 1, 7])
print("\nExample 4:", lowest, highest)

# --- Example 5: slicing, counting, searching ---
data = (1, 2, 2, 3, 2)
print("\nExample 5:", data[1:3], data.count(2), data.index(3))

# --- Example 6: converting between list and tuple ---
as_list = list(data)
as_list.append(99)
print("\nExample 6:", tuple(as_list))

# --- Example 7: tuples as dictionary keys / fixed records ---
person = ("Asha", 21, "Pune")
name, age, city = person
print(f"\nExample 7: {name}, {age}, {city}")
locations = {(0, 0): "origin", (1, 2): "treasure"}
print(locations[(1, 2)])

# --- Common mistakes: immutability ---
print("\nCommon mistakes:")
try:
    colors[0] = "pink"                 # cannot assign to a tuple item
except TypeError as error:
    print("  TypeError:", error)

try:
    x, y, z = point                    # wrong number of values
except ValueError as error:
    print("  ValueError:", error)

# A tuple holding a list: the tuple is fixed, but the inner list can change
mixed = ([1, 2], "fixed")
mixed[0].append(3)
print("  inner list changed:", mixed)
