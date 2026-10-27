"""String formatting: f-strings, .format(), % formatting, and string methods."""

name = "Asha"
age = 21
price = 1234.5678

# --- Example 1: f-strings (recommended) ---
print("Example 1:")
print(f"My name is {name} and I am {age} years old.")
print(f"Next year I will be {age + 1}.")          # expressions work inside {}
print(f"{name.upper()} has {len(name)} letters.")  # so do method calls

# --- Example 2: number formatting ---
print("\nExample 2:")
print(f"Price: {price:.2f}")          # 2 decimal places -> 1234.57
print(f"Price: {price:,.2f}")         # thousands separator -> 1,234.57
print(f"Percent: {0.256:.1%}")        # 25.6%
print(f"Padded: {7:03d}")             # 007
print(f"Binary of 10: {10:b}")        # 1010

# --- Example 3: alignment and width (nice tables) ---
print("\nExample 3:")
items = [("Pen", 1.5, 10), ("Notebook", 45.0, 3), ("Bag", 899.99, 1)]
print(f"{'Item':<10}{'Price':>10}{'Qty':>5}")
print("-" * 25)
for item, unit_price, qty in items:
    print(f"{item:<10}{unit_price:>10.2f}{qty:>5}")
print(f"{'centered':^25}")

# --- Example 4: str.format() ---
print("\nExample 4:")
print("Hello, {}! You are {}.".format(name, age))
print("{0} likes {1}; {1} likes {0}.".format("Ravi", "Mia"))     # positions
print("{n} scored {s:.1f}".format(n="Ravi", s=88.456))          # names

# --- Example 5: old-style % formatting (you may see it in older code) ---
print("\nExample 5:")
print("Name: %s, Age: %d, Price: %.2f" % (name, age, price))

# --- Example 6: concatenation vs formatting ---
print("\nExample 6:")
print("Age: " + str(age))        # concatenation needs str()
print("Age:", age)               # print adds spaces itself
print(f"Age: {age}")             # f-string handles it

# --- Example 7: useful string methods ---
print("\nExample 7:")
message = "  Hello, Python World  "
print(message.strip())                 # remove surrounding spaces
print(message.lower(), "|", message.title())
print(message.replace("World", "Learner"))
print("a,b,c".split(","))              # ['a', 'b', 'c']
print("-".join(["2025", "01", "31"]))  # 2025-01-31

# --- Example 8: multi-line strings and escapes ---
print("\nExample 8:")
receipt = f"""Receipt
Customer: {name}
Total:    {price:,.2f}"""
print(receipt)
print("Tab:\tafter tab\nNew line, quote: \"hi\"")
print(r"Raw string keeps \n as-is (useful for file paths)")

# --- Example 9: debugging with f"{x=}" ---
print("\nExample 9:")
print(f"{age=}, {name=}")

# --- Common mistakes ---
print("\nCommon mistakes:")
try:
    print("Age: " + age)     # forgetting str()
except TypeError as error:
    print("  TypeError:", error)
print("  Forgot the f prefix: {name}")      # prints {name} literally
print(f"  Literal braces need doubling: {{name}} -> {name}")
