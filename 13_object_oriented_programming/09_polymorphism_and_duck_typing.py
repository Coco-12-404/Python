"""Topics 13-14: Polymorphism and duck typing.

Polymorphism ("many forms"): different classes offer the same method name, so
one piece of code can work with all of them.
Duck typing: "If it walks like a duck and quacks like a duck, it's a duck."
Python cares about what an object CAN DO, not what class it is.
"""

import math


# --- Example 1: polymorphism through inheritance ---
class Shape:
    def area(self):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width, self.height = width, height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base, self.height = base, height

    def area(self):
        return 0.5 * self.base * self.height


print("Example 1: same call, different behaviour")
shapes = [Circle(2), Rectangle(3, 4), Triangle(6, 5)]
for shape in shapes:
    print(f"  {type(shape).__name__:<10} area = {shape.area():.2f}")
# The loop never checks the type. Add a new Shape and the loop still works.
print("  Total area:", round(sum(shape.area() for shape in shapes), 2))


# --- Example 2: polymorphism without a shared parent (duck typing) ---
class Duck:
    def speak(self):
        return "Quack"


class Robot:
    def speak(self):
        return "Beep"


class Person:
    def speak(self):
        return "Hello"


print("\nExample 2: duck typing")
for thing in (Duck(), Robot(), Person()):
    print(" ", thing.speak())      # no common parent needed


# --- Example 3: built-ins are duck typed too ---
print("\nExample 3:")
for sized in ("hello", [1, 2, 3], {"a": 1}, range(10)):
    print(f"  len({sized!r}) = {len(sized)}")


# --- Example 4: practical - payment methods share an interface ---
class CreditCard:
    def pay(self, amount):
        return f"Charged {amount} to credit card"


class UPI:
    def pay(self, amount):
        return f"Paid {amount} via UPI"


class Cash:
    def pay(self, amount):
        return f"Received {amount} in cash"


def checkout(method, amount):
    return method.pay(amount)         # works with anything that has pay()


print("\nExample 4:")
for method in (CreditCard(), UPI(), Cash()):
    print(" ", checkout(method, 250))

# --- Example 5: EAFP - try it, handle failure ---
print("\nExample 5:")


def make_it_speak(thing):
    try:
        return thing.speak()
    except AttributeError:
        return f"{type(thing).__name__} cannot speak"


print(" ", make_it_speak(Duck()))
print(" ", make_it_speak(42))

# --- Common mistakes ---
print("\nCommon mistakes:")
print("  Checking types everywhere (if isinstance(x, Circle) ... elif ...)")
print("  defeats polymorphism; add a method to each class instead.")
try:
    checkout(object(), 10)
except AttributeError as error:
    print("  Missing method:", error)
