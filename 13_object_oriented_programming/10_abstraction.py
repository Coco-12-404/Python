"""Topic 15: Abstraction and abstract base classes (abc).

Abstraction = exposing WHAT an object does while hiding HOW.
An abstract base class (ABC) defines a required interface. It cannot be
instantiated, and subclasses MUST implement every @abstractmethod.

WHY: it catches mistakes early (at object creation) instead of failing later
with a confusing error in the middle of the program.
"""

from abc import ABC, abstractmethod


# --- Example 1: defining an abstract base class ---
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Return the area."""

    @abstractmethod
    def perimeter(self):
        """Return the perimeter."""

    def describe(self):                 # concrete method: shared by all shapes
        return f"{type(self).__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width, self.height = width, height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


print("Example 1:")
for shape in (Rectangle(3, 4), Circle(1)):
    print(" ", shape.describe())

# --- Example 2: you cannot instantiate an abstract class ---
print("\nExample 2:")
try:
    Shape()
except TypeError as error:
    print("TypeError:", error)


# --- Example 3: a subclass that forgets a method is also rejected ---
class IncompleteSquare(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
    # perimeter() missing!


print("\nExample 3:")
try:
    IncompleteSquare(2)
except TypeError as error:
    print("TypeError:", error)


# --- Example 4: practical - payment processors with a guaranteed interface ---
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        ...

    def receipt(self, amount):
        return f"Receipt: {self.pay(amount)}"


class CardProcessor(PaymentProcessor):
    def pay(self, amount):
        return f"{amount} charged to card"


class WalletProcessor(PaymentProcessor):
    def pay(self, amount):
        return f"{amount} deducted from wallet"


print("\nExample 4:")
for processor in (CardProcessor(), WalletProcessor()):
    print(" ", processor.receipt(100))

# --- Example 5: abstract classes can hold shared state ---
print("\nExample 5:")


class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def monthly_pay(self):
        ...


class Salaried(Employee):
    def __init__(self, name, annual):
        super().__init__(name)
        self.annual = annual

    def monthly_pay(self):
        return self.annual / 12


class Hourly(Employee):
    def __init__(self, name, rate, hours):
        super().__init__(name)
        self.rate, self.hours = rate, hours

    def monthly_pay(self):
        return self.rate * self.hours


for worker in (Salaried("Asha", 120000), Hourly("Ravi", 500, 160)):
    print(f"  {worker.name}: {worker.monthly_pay():.2f}")

# --- Common mistakes ---
print("\nCommon mistakes:")
print("  Forgetting to inherit from ABC: @abstractmethod is then NOT enforced.")


class NotEnforced:
    @abstractmethod
    def work(self):
        ...


print("  NotEnforced() created without error:", NotEnforced())
print("  Using ABCs for tiny programs where a plain base class would do.")
