"""while loops: repeat while a condition stays True.

All examples here are non-interactive. See interactive_loop.py for input().
"""

# --- Example 1: basic counter ---
count = 1
print("Example 1:")
while count <= 3:
    print("  count =", count)
    count += 1               # without this the loop never ends!

# --- Example 2: countdown ---
print("\nExample 2:")
seconds = 3
while seconds > 0:
    print(" ", seconds)
    seconds -= 1
print("  Liftoff!")

# --- Example 3: accumulate until a limit ---
print("\nExample 3:")
total = 0
number = 1
while total + number <= 20:
    total += number
    number += 1
print(f"  added 1..{number - 1}, total = {total}")

# --- Example 4: break inside while True ---
print("\nExample 4:")
attempts = 0
while True:
    attempts += 1
    if attempts * attempts > 50:
        break
print("  first number whose square exceeds 50:", attempts)

# --- Example 5: continue ---
print("\nExample 5:")
i = 0
while i < 6:
    i += 1
    if i % 2 == 0:
        continue             # skip even numbers
    print("  odd:", i)

# --- Example 6: practical - compound interest doubling time ---
print("\nExample 6:")
balance, years = 1000.0, 0
while balance < 2000:
    balance *= 1.07
    years += 1
print(f"  at 7% it takes {years} years to double ({balance:.2f})")

# --- Example 7: digit sum with while ---
print("\nExample 7:")
value = 4821
digit_sum = 0
while value > 0:
    digit_sum += value % 10
    value //= 10
print("  digit sum of 4821 =", digit_sum)

# --- Example 8: Collatz sequence ---
print("\nExample 8:")
n = 6
steps = [n]
while n != 1:
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    steps.append(n)
print(" ", steps)

# --- Example 9: while-else ---
print("\nExample 9:")
k = 0
while k < 3:
    k += 1
else:
    print("  loop finished without break")

# --- Common mistakes ---
# 1. Infinite loop: forgetting to change the variable used in the condition.
# 2. Off-by-one: `< 5` vs `<= 5`.
# 3. Using `while` where a `for` over a range is clearer.
print("\nCommon mistakes: see the comments above (an infinite loop is not run here).")
