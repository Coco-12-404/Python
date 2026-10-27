"""for loops: repeat code for each item in a sequence."""

# --- Example 1: looping over a list and a string ---
print("Example 1:")
for fruit in ["apple", "banana", "cherry"]:
    print(" ", fruit)
for letter in "Hi!":
    print(" ", letter)

# --- Example 2: range() ---
print("\nExample 2:")
print(list(range(5)))            # 0..4
print(list(range(2, 8)))         # 2..7
print(list(range(10, 0, -3)))    # counting down: 10, 7, 4, 1
for number in range(1, 4):
    print(f"  {number} x 7 = {number * 7}")

# --- Example 3: accumulating a total ---
total = 0
for price in [120, 80, 45]:
    total += price
print("\nExample 3: total =", total)

# --- Example 4: enumerate() gives index + value ---
print("\nExample 4:")
for position, name in enumerate(["Ana", "Ben", "Cara"], start=1):
    print(f"  {position}. {name}")

# --- Example 5: zip() loops over two lists together ---
print("\nExample 5:")
students = ["Ana", "Ben"]
marks = [88, 92]
for student, mark in zip(students, marks):
    print(f"  {student}: {mark}")

# --- Example 6: break, continue, and for-else ---
print("\nExample 6:")
for n in range(1, 10):
    if n == 3:
        continue                 # skip 3
    if n == 6:
        break                    # stop the loop at 6
    print("  n =", n)

for n in [4, 6, 8]:
    if n % 2 == 1:
        print("  found an odd number")
        break
else:                            # runs only if the loop did NOT break
    print("  no odd numbers found")

# --- Example 7: nested loops (multiplication table) ---
print("\nExample 7:")
for row in range(1, 4):
    line = ""
    for col in range(1, 4):
        line += f"{row * col:>4}"
    print(line)

# --- Example 8: patterns ---
print("\nExample 8:")
for stars in range(1, 5):
    print("  " + "*" * stars)

# --- Example 9: practical - find primes up to 30 ---
print("\nExample 9: primes")
primes = []
for candidate in range(2, 31):
    is_prime = True
    for divisor in range(2, int(candidate ** 0.5) + 1):
        if candidate % divisor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(candidate)
print(" ", primes)

# --- Common mistakes ---
print("\nCommon mistakes:")
print("  range(5) stops BEFORE 5:", list(range(5)))
numbers = [1, 2, 3, 4]
for n in numbers[:]:              # loop over a COPY if you remove while looping
    if n % 2 == 0:
        numbers.remove(n)
print("  safe removal:", numbers)
