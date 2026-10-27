"""Interactive loop: a number guessing game plus a running-total calculator.

Run: python interactive_loop.py
The checking logic lives in small functions so it can be tested without typing.
"""

import random


def evaluate_guess(guess, secret):
    """Return 'low', 'high' or 'correct'."""
    if guess < secret:
        return "low"
    if guess > secret:
        return "high"
    return "correct"


def parse_number(text):
    """Return a float from text, or None if invalid."""
    try:
        return float(text)
    except ValueError:
        return None


def guessing_game(max_tries=5):
    secret = random.randint(1, 20)
    print("I'm thinking of a number from 1 to 20.")
    for attempt in range(1, max_tries + 1):
        text = input(f"Guess {attempt}/{max_tries}: ").strip()
        if not text.isdigit():
            print("  Numbers only, please.")
            continue                      # invalid input still uses an attempt
        result = evaluate_guess(int(text), secret)
        if result == "correct":
            print(f"  Correct! You needed {attempt} tries.")
            return
        print("  Too low." if result == "low" else "  Too high.")
    print(f"Out of tries. The number was {secret}.")


def running_total():
    print("Enter numbers to add. Type 'done' to finish.")
    total = 0.0
    while True:
        text = input("> ").strip().lower()
        if text == "done":
            break
        value = parse_number(text)
        if value is None:
            print("  That's not a number.")
            continue
        total += value
    print(f"Total: {total}")


if __name__ == "__main__":
    guessing_game()
    running_total()
