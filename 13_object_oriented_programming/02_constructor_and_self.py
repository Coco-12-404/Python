"""Topics 3-4: The __init__() constructor and the self parameter.

WHY: __init__ runs automatically when an object is created, so every object
starts life with the data it needs. `self` is how a method refers to the
particular object it was called on.
"""


# --- Example 1: a constructor ---
class Employee:
    def __init__(self, name, salary):
        # self.name is an INSTANCE ATTRIBUTE: stored on this one object
        self.name = name
        self.salary = salary

    def describe(self):
        return f"{self.name} earns {self.salary}"


print("Example 1:")
asha = Employee("Asha", 50000)       # __init__ is called for us
ravi = Employee("Ravi", 42000)
print(asha.describe())
print(ravi.describe())

# --- Example 2: what `self` really is ---
print("\nExample 2:")


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self        # returning self allows chaining (optional trick)


first, second = Counter(), Counter()
first.increment()
first.increment()
second.increment()
print(first.count, second.count)   # 2 1  -> each object has its own self.count
# first.increment() is the same as Counter.increment(first)
Counter.increment(second)
print("Explicit call:", second.count)
print("Chaining (optional):", Counter().increment().increment().count)


# --- Example 3: default values and validation in the constructor ---
class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Opening balance cannot be negative")
        self.owner = owner
        self.balance = balance
        self.transactions = []       # every object gets its OWN list


print("\nExample 3:")
account = BankAccount("Meera")
print(account.owner, account.balance, account.transactions)
try:
    BankAccount("Bad", -50)
except ValueError as error:
    print("Rejected:", error)

# --- Example 4: keyword arguments work too ---
print("\nExample 4:")
vip = BankAccount(balance=1000, owner="Dev")
print(vip.owner, vip.balance)

# --- Common mistakes ---
print("\nCommon mistakes:")
try:
    Employee("Only name")            # missing a required argument
except TypeError as error:
    print("  TypeError:", error)


class Forgetful:
    def __init__(self, value):
        value = value                # BUG: sets a local variable, not an attribute


try:
    print(Forgetful(5).value)
except AttributeError as error:
    print("  Forgot self.:", error)

# Another classic: __init__ must not return a value, and the name has two
# underscores on each side (__init__, not _init_).
# Expected: Example 1 prints "Asha earns 50000" and "Ravi earns 42000".
