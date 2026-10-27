"""Topics 6-7: Class attributes, class methods, and static methods.

Instance attribute : belongs to ONE object            (self.name)
Class attribute    : shared by ALL objects of a class (Employee.company)
Instance method    : receives the object   -> def method(self)
Class method       : receives the class    -> @classmethod def method(cls)
Static method      : receives nothing      -> @staticmethod def method()
"""


class Employee:
    company = "Acme Corp"          # class attribute: one copy shared by everyone
    employee_count = 0             # shared counter
    raise_percent = 5

    def __init__(self, name, salary):
        self.name = name           # instance attributes
        self.salary = salary
        Employee.employee_count += 1   # update the shared value via the class

    # --- instance method: needs self ---
    def apply_raise(self):
        self.salary += self.salary * self.raise_percent / 100

    # --- class method: needs the class, not a specific object ---
    @classmethod
    def from_string(cls, text):
        """Alternative constructor: Employee.from_string('Asha-50000')."""
        name, salary = text.split("-")
        return cls(name, int(salary))      # cls(...) works even for subclasses

    @classmethod
    def set_raise_percent(cls, percent):
        if percent < 0:
            raise ValueError("Raise cannot be negative")
        cls.raise_percent = percent

    # --- static method: a helper that needs neither self nor cls ---
    @staticmethod
    def is_workday(day_name):
        return day_name.lower() not in ("saturday", "sunday")


print("Example 1: class vs instance attributes")
asha = Employee("Asha", 50000)
ravi = Employee("Ravi", 40000)
print(asha.company, ravi.company, Employee.company)
print("Employees created:", Employee.employee_count)    # 2

print("\nExample 2: changing a class attribute affects everyone")
Employee.company = "Globex"
print(asha.company, ravi.company)                       # Globex Globex

print("\nExample 3: class method as alternative constructor")
meera = Employee.from_string("Meera-60000")
print(meera.name, meera.salary, Employee.employee_count)

print("\nExample 4: class method updating shared setting")
Employee.set_raise_percent(10)
asha.apply_raise()
print(asha.salary)                                      # 55000.0

print("\nExample 5: static method (plain function that lives in the class)")
print(Employee.is_workday("Monday"), Employee.is_workday("Sunday"))
print(asha.is_workday("Friday"))                        # can also call on an object

print("\nExample 6: when to use which?")
print("  instance method -> needs this object's data")
print("  class method    -> needs class-level data or builds objects")
print("  static method   -> related utility, uses neither")

# --- Common mistakes ---
print("\nCommon mistakes:")
# 1. Assigning through an instance creates a NEW instance attribute that
#    shadows the class attribute instead of changing it.
asha.raise_percent = 99
print("  asha:", asha.raise_percent, "| class:", Employee.raise_percent,
      "| ravi:", ravi.raise_percent)

# 2. Mutable class attributes are shared by all objects - usually a bug.


class BadTeam:
    members = []                       # shared list!


a, b = BadTeam(), BadTeam()
a.members.append("Asha")
print("  b.members unexpectedly contains:", b.members)


class GoodTeam:
    def __init__(self):
        self.members = []              # each object gets its own list


c, d = GoodTeam(), GoodTeam()
c.members.append("Asha")
print("  GoodTeam d.members:", d.members)

# Expected: Example 1 prints "Acme Corp Acme Corp Acme Corp" then "Employees created: 2".
