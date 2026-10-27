"""Topics 1-2: What is OOP? Classes vs objects, defining classes, creating objects.

WHY OOP? Real programs model things (employees, accounts, books). A class bundles
the DATA a thing has (attributes) with the ACTIONS it can do (methods), so related
code lives together and is easy to reuse.

A class is a blueprint. An object (instance) is a thing built from that blueprint.
"""


# --- Example 1: the simplest class ---
class Dog:
    """Blueprint for dogs."""

    def bark(self):
        print("Woof!")


print("Example 1:")
rex = Dog()          # create an object (an instance of Dog)
fido = Dog()         # a second, separate object
rex.bark()
print(type(rex))     # <class '__main__.Dog'>
print(isinstance(rex, Dog), rex is fido)   # True False -> two different objects

# --- Example 2: objects hold their own data ---
print("\nExample 2:")
rex.name = "Rex"             # attaching attributes directly works...
fido.name = "Fido"
print(rex.name, fido.name)   # ...but each object has its own copy
# This is clumsy: a Dog without a name could be created by accident.
# The constructor (next file) solves this.


# --- Example 3: a class with data and behaviour together ---
class Employee:
    """A tiny employee model."""

    def set_details(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, percent):
        self.salary += self.salary * percent / 100

    def describe(self):
        return f"{self.name} earns {self.salary:.2f}"


print("\nExample 3:")
asha = Employee()
asha.set_details("Asha", 50000)
asha.give_raise(10)
print(asha.describe())       # Asha earns 55000.00

# --- Example 4: classes vs objects in one picture ---
print("\nExample 4:")
print("Employee is the class:", Employee)
print("asha is an object   :", type(asha).__name__)
print("Same class, different objects:", Employee() is Employee())

# --- Common mistakes ---
print("\nCommon mistakes:")
try:
    Dog.bark()                 # calling a method on the class, not an object
except TypeError as error:
    print("  TypeError:", error)

try:
    print(Employee().salary)   # attribute never set on this object
except AttributeError as error:
    print("  AttributeError:", error)
print("  Class names use CapWords (Dog), objects/variables use snake_case (rex).")

# Expected output (first lines):
#   Example 1:
#   Woof!
#   <class '__main__.Dog'>
#   True False
