"""Comments and docstrings.

This text in triple quotes at the top of a file is a *docstring*.
It describes what the file does.
"""

# --- Example 1: single-line comments ---
# A comment starts with # and is ignored by Python.
price = 20  # inline comment: explain WHY, not the obvious WHAT
print("Example 1:", price)

# --- Example 2: comments that explain a reason ---
# Bad:  add 1 to index
# Good: lists are 0-indexed, so add 1 to show a human-friendly position
index = 4
print("Example 2: position", index + 1)

# --- Example 3: block comments for a multi-step task ---
# Step 1: set the base values
# Step 2: apply a 10% discount
# Step 3: print the final price
base_price = 200
discounted = base_price * 0.9
print("Example 3:", discounted)

# --- Example 4: commenting out code while debugging ---
print("Example 4: this line runs")
# print("this line is disabled and does not run")


# --- Example 5: docstrings document functions ---
def area_of_circle(radius):
    """Return the area of a circle with the given radius."""
    return 3.14159 * radius ** 2  # 3.14159 approximates pi


print("Example 5:", area_of_circle(2))
print("The docstring is available as data:", area_of_circle.__doc__)

# --- Example 6: TODO / NOTE conventions ---
# TODO: handle negative radius values
# NOTE: tools and editors often highlight these markers

# --- Common mistakes ---
# 1. A # inside a string is NOT a comment:
print("Common mistake: this # is part of the text")
# 2. Outdated comments are worse than none - update them when code changes.
# 3. Don't comment the obvious:   x = 5  # set x to 5
