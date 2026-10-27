"""Topic 5: Instance attributes and instance methods.

Instance attributes = data belonging to ONE object.
Instance methods    = functions that work on that object's data through `self`.
"""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    # --- instance methods ---
    def deposit(self, amount):
        if amount <= 0:
            print("  Deposit must be positive.")
            return False
        self.balance += amount
        self.history.append(f"deposit {amount}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("  Withdrawal must be positive.")
            return False
        if amount > self.balance:
            print(f"  Insufficient funds: balance is {self.balance}, requested {amount}.")
            return False
        self.balance -= amount
        self.history.append(f"withdraw {amount}")
        return True

    def summary(self):
        return f"{self.owner}: balance {self.balance}"


print("Example 1: methods change the object's state")
account = BankAccount("Asha", 1000)
account.deposit(500)
account.withdraw(200)
print(account.summary())           # Asha: balance 1300
print(account.history)             # ['deposit 500', 'withdraw 200']

print("\nExample 2: invalid operations are rejected")
account.withdraw(99999)
account.deposit(-5)

print("\nExample 3: objects are independent")
other = BankAccount("Ravi")
other.deposit(50)
print(account.balance, other.balance)    # 1300 50

print("\nExample 4: methods can call other methods")


class Vehicle:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount

    def brake(self):
        self.speed = 0

    def emergency_stop(self):
        self.brake()                       # call another method through self
        return f"{self.brand} stopped"


car = Vehicle("Toyota")
car.accelerate(60)
print(car.speed, car.emergency_stop(), car.speed)   # 60 Toyota stopped 0

print("\nExample 5: attributes can be added later (works, but avoid it)")
car.colour = "red"            # not defined in __init__ -> hard to keep track of
print(car.colour)

print("\nExample 6: inspecting an object")
print(vars(account))          # attribute names and values as a dict
print(hasattr(account, "owner"), hasattr(account, "email"))

# --- Common mistakes ---
print("\nCommon mistakes:")
try:
    account.deposit()              # forgot the amount argument
except TypeError as error:
    print("  TypeError:", error)
print("  Forgetting `self.` inside a method makes a local variable that vanishes:")


class Broken:
    def __init__(self):
        self.total = 0

    def add(self, n):
        total = self.total + n      # BUG: should be self.total = ...


b = Broken()
b.add(5)
print("  total after add(5):", b.total, "(expected 5)")
