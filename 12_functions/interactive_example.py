"""Interactive functions: a small unit-converter menu.

Run: python interactive_example.py
"""


def km_to_miles(km):
    return km * 0.621371


def miles_to_km(miles):
    return miles / 0.621371


def kg_to_pounds(kg):
    return kg * 2.20462


def read_number(prompt):
    """Ask until the user enters a valid number."""
    while True:
        text = input(prompt).strip()
        try:
            return float(text)
        except ValueError:
            print("  Please enter a number.")


def main():
    menu = {
        "1": ("Kilometres to miles", km_to_miles, "mi"),
        "2": ("Miles to kilometres", miles_to_km, "km"),
        "3": ("Kilograms to pounds", kg_to_pounds, "lb"),
    }
    while True:
        print("\nUnit converter")
        for key, (label, _, _) in menu.items():
            print(f"  {key}. {label}")
        print("  q. Quit")
        choice = input("Choose: ").strip().lower()
        if choice == "q":
            print("Bye!")
            break
        if choice not in menu:
            print("  Invalid choice.")
            continue
        label, convert, unit = menu[choice]
        value = read_number("Value: ")
        print(f"  {label}: {convert(value):.2f} {unit}")


if __name__ == "__main__":
    main()
