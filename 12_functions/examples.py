"""Functions: reusable blocks of code."""


# --- Example 1: defining and calling ---
def greet():
    print("Hello!")


print("Example 1:")
greet()
greet()


# --- Example 2: parameters and return values ---
def add(a, b):
    """Return the sum of a and b."""
    return a + b


result = add(3, 4)
print("\nExample 2:", result)


# --- Example 3: default arguments ---
def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print("\nExample 3:")
print(greet_user("Asha"))
print(greet_user("Asha", "Namaste"))


# --- Example 4: keyword arguments (order does not matter) ---
def describe_pet(animal, name, age=1):
    return f"{name} is a {age}-year-old {animal}."


print("\nExample 4:")
print(describe_pet(name="Rex", animal="dog", age=3))
print(describe_pet("cat", "Tom"))


# --- Example 5: returning multiple values (a tuple) ---
def min_max_average(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)


low, high, average = min_max_average([4, 8, 15])
print(f"\nExample 5: low={low}, high={high}, average={average:.2f}")


# --- Example 6: practical - validation helpers ---
def is_even(number):
    return number % 2 == 0


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def average_of(numbers):
    """Return the average, or None for an empty list."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


print("\nExample 6:")
print(is_even(10), celsius_to_fahrenheit(100), average_of([]), average_of([2, 4]))


# --- Example 7: functions calling functions ---
def square(n):
    return n * n


def sum_of_squares(numbers):
    total = 0
    for n in numbers:
        total += square(n)
    return total


print("\nExample 7:", sum_of_squares([1, 2, 3]))


# --- Example 8: variable scope ---
counter = 0       # global


def show_scope():
    local_value = 5          # exists only inside the function
    return local_value + counter


print("\nExample 8:", show_scope())


# --- Example 9: *args for any number of arguments (optional) ---
def total_of(*numbers):
    return sum(numbers)


print("\nExample 9 (optional):", total_of(1, 2, 3, 4))


# --- Example 10: a function that prints vs one that returns ---
def print_double(n):
    print(n * 2)         # shows a value but gives back None


def return_double(n):
    return n * 2         # gives a value you can reuse


print("\nExample 10:")
print_double(4)
value = return_double(4) + 1
print("Reusable result:", value)

# --- Common mistakes ---
print("\nCommon mistakes:")
try:
    add(1)                                  # missing argument
except TypeError as error:
    print("  TypeError:", error)

print("  Forgetting return gives:", print_double(1))   # prints 2, then None


def add_item_wrongly(item, items=[]):        # mutable default is shared!
    items.append(item)
    return items


print("  Shared default list:", add_item_wrongly("a"), add_item_wrongly("b"))


def add_item_correctly(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


print("  Fixed:", add_item_correctly("a"), add_item_correctly("b"))
