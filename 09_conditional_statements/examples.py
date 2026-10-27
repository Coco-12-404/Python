"""Conditional statements: if / elif / else. Non-interactive - values are set in code."""


# --- Example 1: if / else ---
def check_voting(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible yet"


print("Example 1:", check_voting(20), "|", check_voting(15))


# --- Example 2: elif chain (grades) ---
def grade_for(score):
    if score < 0 or score > 100:
        return "Invalid score"          # handle edge cases first
    elif score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "Fail"


print("\nExample 2:")
for test_score in (95, 80, 55, 20, 101, -1):
    print(f"  {test_score:>4} -> {grade_for(test_score)}")

# --- Example 3: nested if ---
age, has_id = 22, True
print("\nExample 3:")
if age >= 18:
    if has_id:
        print("  Entry allowed")
    else:
        print("  Bring an ID")
else:
    print("  Too young")

# --- Example 4: combining conditions (flatter than nesting) ---
print("\nExample 4:")
if age >= 18 and has_id:
    print("  Entry allowed")

# --- Example 5: conditional expression (ternary) ---
number = 7
parity = "even" if number % 2 == 0 else "odd"
print("\nExample 5:", number, "is", parity)

# --- Example 6: truthiness in conditions ---
print("\nExample 6:")
shopping_cart = []
if shopping_cart:
    print("  Cart has items")
else:
    print("  Cart is empty")          # an empty list is falsy


# --- Example 7: practical - shipping cost ---
def shipping_cost(weight_kg, is_member):
    if weight_kg <= 0:
        return None                   # invalid input
    if is_member:
        return 0
    if weight_kg <= 1:
        return 40
    elif weight_kg <= 5:
        return 90
    return 150


print("\nExample 7:")
print("  Member 3kg:", shipping_cost(3, True))
print("  Guest 3kg:", shipping_cost(3, False))
print("  Guest 8kg:", shipping_cost(8, False))
print("  Invalid:", shipping_cost(-2, False))

# --- Example 8: match statement (optional, Python 3.10+) ---
# Optional: an alternative to long elif chains comparing one value.
command = "stop"
match command:
    case "go":
        print("\nExample 8: moving")
    case "stop":
        print("\nExample 8: stopping")
    case _:
        print("\nExample 8: unknown command")

# --- Example 9: FizzBuzz-style logic (order matters!) ---
print("\nExample 9:")
for n in (3, 5, 15, 7):
    if n % 15 == 0:
        print("  ", n, "FizzBuzz")
    elif n % 3 == 0:
        print("  ", n, "Fizz")
    elif n % 5 == 0:
        print("  ", n, "Buzz")
    else:
        print("  ", n)

# --- Common mistakes ---
print("\nCommon mistakes:")
x = 5
# 1. Using = instead of == in a condition is a SyntaxError:  if x = 5:
# 2. Wrong order: checking score >= 50 before score >= 90 makes every pass a "C".
# 3. Comparing to True/False explicitly is redundant: write `if is_ready:`.
# 4. `if x == 1 or 2:` is always truthy! Write `if x == 1 or x == 2:` or `x in (1, 2)`.
print("  Buggy check says:", "yes" if (x == 1 or 2) else "no", "(even though x is 5)")
print("  Correct check says:", "yes" if x in (1, 2) else "no")
