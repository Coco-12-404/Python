"""Topics 10-11: Inheritance - single, multilevel, and multiple.

WHY: a child class reuses (inherits) the attributes and methods of a parent,
so shared code is written once. Use it for an "is-a" relationship:
a Dog IS an Animal.
"""


# --- Example 1: single inheritance ---
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"


class Dog(Animal):                # Dog inherits from Animal
    def bark(self):
        return f"{self.name} says Woof!"


print("Example 1: single inheritance")
rex = Dog("Rex")
print(rex.eat())          # inherited
print(rex.bark())         # its own
print(isinstance(rex, Dog), isinstance(rex, Animal), issubclass(Dog, Animal))


# --- Example 2: extending __init__ with super() ---
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)      # reuse the parent's setup
        self.team_size = team_size          # add something new


print("\nExample 2:")
boss = Manager("Meera", 90000, 5)
print(boss.name, boss.salary, boss.team_size)


# --- Example 3: multilevel inheritance (a chain) ---
class Vehicle:
    def start(self):
        return "engine on"


class Car(Vehicle):
    def drive(self):
        return "driving"


class ElectricCar(Car):
    def charge(self):
        return "charging"


print("\nExample 3: multilevel")
tesla = ElectricCar()
print(tesla.start(), "|", tesla.drive(), "|", tesla.charge())
print("Chain:", [cls.__name__ for cls in ElectricCar.__mro__])


# --- Example 4: multiple inheritance ---
class Flyer:
    def fly(self):
        return "flying"


class Swimmer:
    def swim(self):
        return "swimming"


class Duck(Flyer, Swimmer):         # inherits from two parents
    pass


print("\nExample 4: multiple inheritance")
duck = Duck()
print(duck.fly(), "and", duck.swim())


# --- Example 5: Method Resolution Order (MRO) ---
# When two parents define the same method, Python searches in a fixed order.
class A:
    def who(self):
        return "A"


class B(A):
    def who(self):
        return "B"


class C(A):
    def who(self):
        return "C"


class D(B, C):          # the "diamond": D -> B -> C -> A
    pass


print("\nExample 5: MRO")
print(D().who())                                # B (left parent wins)
print([cls.__name__ for cls in D.__mro__])     # ['D', 'B', 'C', 'A', 'object']
# Tip: keep multiple inheritance simple; use it for small "mixin" helpers.

# --- Common mistakes ---
print("\nCommon mistakes:")
try:
    class Broken(Employee):
        def __init__(self, name, salary, bonus):
            self.bonus = bonus          # forgot super().__init__()

    print(Broken("Ravi", 1, 2).name)
except AttributeError as error:
    print("  Forgot super().__init__():", error)
print("  Inheriting just to reuse code when it isn't 'is-a' -> use composition.")
print("  Deep chains (5+ levels) become hard to follow.")
