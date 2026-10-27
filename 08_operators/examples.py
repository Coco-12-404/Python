"""Operators: arithmetic, assignment, comparison, logical, membership."""

# --- Example 1: arithmetic ---
a, b = 17, 5
print("Example 1:")
print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)      # true division -> always float
print("a // b =", a // b)     # floor division -> 3
print("a % b  =", a % b)      # remainder -> 2
print("a ** b =", a ** b)     # power

# --- Example 2: precedence ---
print("\nExample 2:")
print(2 + 3 * 4)        # 14: * before +
print((2 + 3) * 4)      # 20: parentheses first
print(2 ** 3 ** 2)      # 512: ** is right-to-left
print(-3 ** 2)          # -9: ** before unary minus

# --- Example 3: assignment shortcuts ---
total = 10
total += 5      # same as total = total + 5
total -= 3
total *= 2
total //= 4
total **= 2
print("\nExample 3:", total)

# --- Example 4: practical - splitting seconds into h:m:s ---
seconds = 3725
hours, remainder = divmod(seconds, 3600)
minutes, secs = divmod(remainder, 60)
print(f"\nExample 4: {hours}h {minutes}m {secs}s")

# --- Example 5: modulo uses ---
print("\nExample 5:")
number = 14
print("even" if number % 2 == 0 else "odd")
print("Day after 5 days from day 6 (0-6 week):", (6 + 5) % 7)

# --- Example 6: comparison and logical operators ---
print("\nExample 6:")
print(5 > 3, 5 == 5.0, "a" != "b")
print(5 > 3 and 2 > 4, 5 > 3 or 2 > 4, not 5 > 3)

# --- Example 7: string and list operators ---
print("\nExample 7:")
print("Hi " * 3)
print("Hello, " + "World")
print([1, 2] + [3])
print([0] * 4)

# --- Example 8: membership and identity ---
print("\nExample 8:")
print("py" in "python", 3 in [1, 2, 3], "x" not in "abc")
print(None is None)

# --- Example 9: rounding and built-in helpers ---
print("\nExample 9:")
print(round(3.14159, 2), abs(-7), pow(2, 5), max(3, 9), min(3, 9))
print(7 / 2, 7 // 2, -7 // 2)       # floor goes DOWN: -4

# --- Example 10: bitwise (optional, rarely needed at this stage) ---
print("\nExample 10 (optional):", 5 & 3, 5 | 3, 5 ^ 3)

# --- Common mistakes ---
print("\nCommon mistakes:")
try:
    print(10 / 0)
except ZeroDivisionError as error:
    print("  ZeroDivisionError:", error)

try:
    print("5" + 5)
except TypeError as error:
    print("  TypeError:", error)

print("  Float precision:", 0.1 + 0.2)
print("  Integer vs true division:", 7 // 2, "vs", 7 / 2)
