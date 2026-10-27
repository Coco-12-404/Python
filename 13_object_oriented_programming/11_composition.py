"""Topic 16: Composition vs. inheritance.

Inheritance = "is-a"  (a Dog IS an Animal)
Composition = "has-a" (a Car HAS an Engine)

Prefer composition when the relationship is "has-a" or when you just want to
reuse behaviour. It keeps classes small, flexible, and easy to change.
"""


# --- Example 1: composition - Car has an Engine ---
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        self.running = False

    def start(self):
        self.running = True
        return "Engine started"

    def stop(self):
        self.running = False
        return "Engine stopped"


class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine            # a Car HAS an Engine

    def start(self):
        return f"{self.brand}: {self.engine.start()}"      # delegate the work


print("Example 1:")
car = Car("Toyota", Engine(120))
print(car.start(), "| engine running:", car.engine.running)


# --- Example 2: swapping parts easily ---
class ElectricMotor:
    horsepower = 200
    running = False

    def start(self):
        self.running = True
        return "Motor humming"


print("\nExample 2:")
print(Car("Tesla", ElectricMotor()).start())   # same Car, different part


# --- Example 3: the wrong way - inheriting for convenience ---
class Stack(list):          # a Stack IS-A list? Then it exposes insert(), sort()...
    def push(self, item):
        self.append(item)


bad_stack = Stack()
bad_stack.push(1)
bad_stack.push(2)
bad_stack.insert(0, 99)     # breaks the "last in, first out" promise
print("\nExample 3: inherited stack leaks list methods:", list(bad_stack))


# --- Example 4: the better way - composition ---
class SafeStack:
    def __init__(self):
        self._items = []        # HAS a list, exposes only what it wants

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def __len__(self):
        return len(self._items)


print("\nExample 4:")
stack = SafeStack()
stack.push("a")
stack.push("b")
print(stack.pop(), len(stack), hasattr(stack, "insert"))   # b 1 False


# --- Example 5: practical - ShoppingCart has Items ---
class Item:
    def __init__(self, name, price):
        self.name, self.price = name, price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item, quantity=1):
        self.items.append((item, quantity))

    def total(self):
        return sum(item.price * quantity for item, quantity in self.items)


print("\nExample 5:")
cart = ShoppingCart()
cart.add(Item("Pen", 10), 3)
cart.add(Item("Book", 250))
print("Cart total:", cart.total())     # 280

# --- Rule of thumb ---
print("\nRule of thumb:")
print("  Ask 'is-a' or 'has-a'? If you can't say 'X is a kind of Y', use composition.")
print("  Inheritance couples child to parent; composition lets you swap parts.")

# --- Common mistakes ---
print("\nCommon mistakes:")
print("  Making Car inherit from Engine just to reuse start(): a car is not an engine.")
print("  Reaching deep into parts (car.engine.fuel.tank.level) - add a method instead.")
