"""Variables: names that point to values."""

# --- Example 1: creating variables and the basic types ---
name = "Asha"          # str (text)
age = 21               # int (whole number)
height_m = 1.62        # float (decimal number)
is_student = True      # bool (True / False)

print("Example 1: basic types")
print(name, type(name))
print(age, type(age))
print(height_m, type(height_m))
print(is_student, type(is_student))

# --- Example 2: variables can be reassigned (even to a different type) ---
score = 10
score = score + 5      # use the old value to compute the new one
print("\nExample 2: reassignment ->", score)
score = "ten"          # allowed in Python, but usually confusing
print("Now score is a", type(score).__name__)

# --- Example 3: multiple assignment and swapping ---
x, y, z = 1, 2, 3
a = b = 0              # both names point to 0
print("\nExample 3:", x, y, z, a, b)
x, y = y, x            # swap without a temporary variable
print("After swap: x =", x, "y =", y)

# --- Example 4: practical use - a simple price calculation ---
item_price = 49.99
quantity = 3
tax_rate = 0.08
subtotal = item_price * quantity
total = subtotal * (1 + tax_rate)
print("\nExample 4: total price =", round(total, 2))

# --- Example 5: type conversion (casting) ---
text_number = "42"
real_number = int(text_number)   # str -> int
print("\nExample 5:", real_number + 8)        # 50
print(str(3.5) + " is now text")
print(float("2.5") * 2)

# --- Example 6: naming rules and conventions ---
user_name = "snake_case is the Python style"   # good
MAX_ATTEMPTS = 3                                # CONSTANT by convention
print("\nExample 6:", user_name, "|", MAX_ATTEMPTS)

# --- Common mistakes (shown safely) ---
print("\nCommon mistakes:")
try:
    print("Age: " + age)                # str + int -> TypeError
except TypeError as error:
    print("  TypeError:", error)

try:
    print(undefined_name)               # never created -> NameError
except NameError as error:
    print("  NameError:", error)

try:
    int("hello")                        # cannot convert -> ValueError
except ValueError as error:
    print("  ValueError:", error)

# Invalid names (would be SyntaxError): 2cool = 1, my-var = 1, class = 1
# Names are case-sensitive: Age and age are different variables.
