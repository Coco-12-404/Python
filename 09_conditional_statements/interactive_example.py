"""Interactive conditionals: a simple ticket price calculator.

Run: python interactive_example.py
The decision logic lives in ticket_price() so it can be tested without typing.
"""


def ticket_price(age, is_weekend):
    """Return the ticket price in rupees, or None for an invalid age."""
    if age < 0 or age > 120:
        return None
    if age < 5:
        price = 0
    elif age < 18:
        price = 100
    elif age >= 60:
        price = 120
    else:
        price = 200
    if is_weekend and price > 0:
        price += 50                    # weekend surcharge (not for free tickets)
    return price


def main():
    raw_age = input("Enter your age: ").strip()
    if not raw_age.isdigit():          # rejects "abc", "-3", "2.5", and ""
        print("Please enter a whole, non-negative number.")
        return
    is_weekend = input("Is it the weekend? (y/n): ").strip().lower() == "y"

    price = ticket_price(int(raw_age), is_weekend)
    if price is None:
        print("That age does not look right.")
    elif price == 0:
        print("Free entry!")
    else:
        print(f"Your ticket costs Rs. {price}")


if __name__ == "__main__":
    main()
