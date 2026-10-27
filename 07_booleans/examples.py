"""Booleans: True / False, comparisons, and logic."""

# --- Example 1: boolean values and comparisons ---
age = 20
print("Example 1:")
print(age > 18, age == 20, age != 20, age <= 19)
print(type(True))

# --- Example 2: and / or / not ---
has_ticket = True
is_vip = False
print("\nExample 2:")
print(has_ticket and is_vip)       # both must be True
print(has_ticket or is_vip)        # at least one True
print(not has_ticket)              # flips the value

# --- Example 3: truth table ---
print("\nExample 3: truth table for and / or")
for left in (True, False):
    for right in (True, False):
        print(f"{left!s:<6} {right!s:<6} and={left and right!s:<6} or={left or right}")

# --- Example 4: truthy and falsy values ---
print("\nExample 4: bool() of different values")
for value in (0, 1, -5, 0.0, "", "hi", [], [0], None, {}):
    print(f"{value!r:>6} -> {bool(value)}")
# Falsy: 0, 0.0, "", [], (), {}, set(), None, False. Everything else is truthy.

# --- Example 5: chained comparisons ---
temperature = 25
print("\nExample 5:", 20 <= temperature <= 30)    # cleaner than two comparisons

# --- Example 6: membership and identity ---
print("\nExample 6:")
print("a" in "banana", 5 not in [1, 2, 3])
nothing = None
print(nothing is None)                              # use `is` for None

# --- Example 7: short-circuit evaluation ---
print("\nExample 7:")
items = []
print(len(items) > 0 and items[0] == "x")           # safe: second part skipped
username = ""
print("Default name:", username or "Guest")         # `or` gives a fallback

# --- Example 8: practical - login check ---
def can_login(username, password, account_active):
    return bool(username) and len(password) >= 8 and account_active

print("\nExample 8:")
print(can_login("asha", "secret123", True))
print(can_login("", "secret123", True))
print(can_login("asha", "short", True))

# --- Example 9: string methods that return booleans ---
print("\nExample 9:", "123".isdigit(), "abc".isalpha(), "Hello".startswith("He"))

# --- Common mistakes ---
print("\nCommon mistakes:")
print("  Strings 'False' is truthy:", bool("False"))
print("  = vs ==: use == to compare:", 3 == 3)
print("  Float comparison surprise: 0.1 + 0.2 == 0.3 is", 0.1 + 0.2 == 0.3)
print("  Use round() or abs(a-b) < tiny:", round(0.1 + 0.2, 2) == 0.3)
print("  Mixing precedence: not binds tighter than and:", not True and False)
