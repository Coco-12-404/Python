"""Getting user input with input().

Run this file and answer the prompts. The helper functions at the top are
reusable and are also tested without typing in 04_user_input/test_helpers.py.
"""


def parse_int(text):
    """Return an int from text, or None if it is not a valid whole number."""
    try:
        return int(text.strip())
    except ValueError:
        return None


def parse_float(text):
    """Return a float from text, or None if it is not a valid number."""
    try:
        return float(text.strip())
    except ValueError:
        return None


def ask_int(prompt):
    """Keep asking until the user types a valid whole number."""
    while True:
        value = parse_int(input(prompt))
        if value is not None:
            return value
        print("  Please enter a whole number like 5.")


def ask_float(prompt):
    """Keep asking until the user types a valid number."""
    while True:
        value = parse_float(input(prompt))
        if value is not None:
            return value
        print("  Please enter a number like 3.5.")


def ask_yes_no(prompt):
    """Return True for yes, False for no; keep asking on anything else."""
    while True:
        answer = input(prompt + " (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("  Please type y or n.")


def main():
    # Example 1: input() always returns a string
    name = input("What is your name? ").strip()
    print(f"Hello, {name.title() or 'friend'}!")

    # Example 2: convert to int (with validation)
    age = ask_int("How old are you? ")
    print(f"In 10 years you will be {age + 10}.")

    # Example 3: convert to float - a tip calculator
    bill = ask_float("Bill amount: ")
    tip_percent = ask_float("Tip percent (e.g. 10): ")
    tip = bill * tip_percent / 100
    print(f"Tip: {tip:.2f}  Total: {bill + tip:.2f}")

    # Example 4: several values on one line
    raw = input("Enter two numbers separated by a space: ")
    parts = raw.split()
    if len(parts) == 2 and parse_float(parts[0]) is not None and parse_float(parts[1]) is not None:
        first, second = float(parts[0]), float(parts[1])
        print(f"Sum = {first + second}")
    else:
        print("Please enter exactly two numbers next time.")

    # Example 5: yes/no questions
    if ask_yes_no("Do you like Python?"):
        print("Great, keep going!")
    else:
        print("It gets more fun with practice.")

    # Common mistake: forgetting that input() returns text
    typed = "5"
    print("Common mistake:", typed + typed, "(text joined) vs", int(typed) + int(typed), "(numbers added)")


if __name__ == "__main__":
    main()
