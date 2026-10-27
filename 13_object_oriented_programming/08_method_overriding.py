"""Topic 12: Method overriding (and extending with super()).

WHY: a child class can replace a parent's method with a version that suits it,
while the rest of the code keeps calling the same method name.
"""


# --- Example 1: overriding completely ---
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"


class Dog(Animal):
    def speak(self):                      # same name -> overrides parent
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


print("Example 1:")
for pet in (Animal("Generic"), Dog("Rex"), Cat("Tom")):
    print(pet.speak())


# --- Example 2: overriding AND reusing the parent via super() ---
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def pay(self):
        return self.salary

    def describe(self):
        return f"{self.name} ({self.__class__.__name__}) earns {self.pay()}"


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def pay(self):
        return super().pay() + self.bonus    # extend, don't duplicate


print("\nExample 2:")
print(Employee("Asha", 50000).describe())
print(Manager("Meera", 80000, 10000).describe())
# describe() is inherited, yet it calls the overridden pay() for a Manager.


# --- Example 3: overriding in a multi-level hierarchy ---
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width, self.height = width, height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)         # a square is a special rectangle


print("\nExample 3:")
print(Rectangle(3, 4).area(), Square(5).area())

# --- Example 4: checking which method runs ---
print("\nExample 4:")
print(Square.area is Rectangle.area)         # True: Square didn't override it
print(Manager.pay is Employee.pay)           # False: Manager overrode it

# --- Common mistakes ---
print("\nCommon mistakes:")
try:
    Shape().area()
except NotImplementedError as error:
    print("  Base class stub:", error)


class Typo(Animal):
    def speek(self):                         # misspelled -> does NOT override
        return "never called"


print("  Typo in method name:", Typo("Oops").speak())
print("  Changing a method's parameters in a child breaks callers - keep signatures compatible.")
