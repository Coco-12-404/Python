"""Topic 8: Encapsulation and access conventions.

Encapsulation = keeping an object's data together with the methods that use it,
and controlling how outsiders change that data (so it cannot become invalid).

IMPORTANT: Python has NO strict private/protected keywords like Java or C++.
It relies on naming CONVENTIONS and trusts programmers:

    name     public      - part of the official interface
    _name    "protected" - convention: internal, please don't touch from outside
    __name   name-mangled - Python renames it to _ClassName__name to avoid
                            accidental clashes in subclasses. Still reachable!
"""


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner            # public
        self._account_type = "savings"  # protected by convention
        self.__balance = balance      # name-mangled

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance


account = BankAccount("Asha", 1000)

print("Example 1: use the public interface")
account.deposit(500)
print(account.owner, account.get_balance())          # Asha 1500

print("\nExample 2: protected is only a convention")
print(account._account_type)         # works - but you are being told "don't"

print("\nExample 3: name mangling")
try:
    print(account.__balance)         # not found under that name
except AttributeError as error:
    print("AttributeError:", error)
print(account._BankAccount__balance)   # the real (mangled) name still works
print(sorted(name for name in vars(account)))

print("\nExample 4: why bypassing the interface is dangerous")
account._BankAccount__balance = -999     # legal Python, but breaks the rules
print("Corrupted balance:", account.get_balance())

print("\nExample 5: protected attributes in inheritance")


class Person:
    def __init__(self, name):
        self._name = name            # subclasses are expected to use this


class Student(Person):
    def introduce(self):
        return f"I am {self._name}"   # fine: subclass access to _name


print(Student("Ravi").introduce())

print("\nExample 6: mangling avoids accidental clashes")


class Parent:
    def __init__(self):
        self.__secret = "parent"


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__secret = "child"       # separate attribute: _Child__secret


kid = Child()
print(sorted(vars(kid)))

# --- Common mistakes ---
print("\nCommon mistakes:")
print("  Thinking __x is truly private: it is only renamed, not locked.")
print("  Using __x everywhere 'for security': prefer a single _x plus properties.")
print("  Public attribute with no validation lets bad data in:")
account.owner = ""                # nothing stops this - consider a property
print("  owner is now:", repr(account.owner))
# The next file shows @property, the Pythonic way to add validation.
