"""Dictionaries: key -> value pairs."""

# --- Example 1: creating and reading ---
student = {"name": "Asha", "age": 21, "city": "Pune"}
print("Example 1:", student)
print(student["name"])
print(student.get("email"))                 # None instead of an error
print(student.get("email", "not provided")) # custom default

# --- Example 2: adding, updating, removing ---
student["email"] = "asha@example.com"       # add
student["age"] = 22                         # update
removed = student.pop("city")               # remove and return
del student["email"]
print("\nExample 2:", student, "| removed:", removed)

# --- Example 3: looping ---
print("\nExample 3:")
prices = {"apple": 30, "banana": 10, "cherry": 90}
for key in prices:
    print(" key:", key)
for fruit, price in prices.items():
    print(f"  {fruit} costs {price}")
print(list(prices.keys()), list(prices.values()))

# --- Example 4: checking keys ---
print("\nExample 4:")
print("apple" in prices, "mango" in prices)     # checks KEYS
print(len(prices))

# --- Example 5: counting with a dictionary ---
print("\nExample 5: letter frequency")
word = "banana"
counts = {}
for letter in word:
    counts[letter] = counts.get(letter, 0) + 1
print(" ", counts)

# --- Example 6: grouping data ---
print("\nExample 6:")
people = [("Ana", "math"), ("Ben", "art"), ("Cara", "math")]
by_subject = {}
for person, subject in people:
    by_subject.setdefault(subject, []).append(person)
print(" ", by_subject)

# --- Example 7: nested dictionaries ---
print("\nExample 7:")
school = {
    "Ana": {"math": 90, "art": 75},
    "Ben": {"math": 60, "art": 95},
}
print(" ", school["Ben"]["art"])
for name, marks in school.items():
    average = sum(marks.values()) / len(marks)
    print(f"  {name}: average {average:.1f}")

# --- Example 8: merging and copying ---
print("\nExample 8:")
defaults = {"theme": "light", "font": 12}
custom = {"font": 14}
settings = {**defaults, **custom}            # later values win
print(" ", settings)
backup = settings.copy()
backup["theme"] = "dark"
print(" ", settings["theme"], backup["theme"])

# --- Example 9: dictionary comprehension and sorting ---
print("\nExample 9:")
squares = {n: n * n for n in range(1, 6)}
print(" ", squares)
by_price = sorted(prices.items(), key=lambda pair: pair[1])
print(" ", by_price)
print("  most expensive:", max(prices, key=prices.get))

# --- Example 10: simple phone book lookup ---
print("\nExample 10:")
phone_book = {"ana": "555-0101", "ben": "555-0102"}
for lookup in ("Ana", "zed"):
    number = phone_book.get(lookup.lower())
    print(f"  {lookup}: {number if number else 'no entry'}")

# --- Common mistakes ---
print("\nCommon mistakes:")
try:
    print(student["phone"])              # missing key
except KeyError as error:
    print("  KeyError:", error)

try:
    broken = {["a"]: 1}                  # lists cannot be keys
except TypeError as error:
    print("  TypeError:", error)

duplicate = {"a": 1, "a": 2}             # duplicate keys: last one wins
print("  duplicate key keeps last value:", duplicate)
