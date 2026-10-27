"""Topic 9: Getters, setters, and the @property decorator.

WHY: you want attribute-style access (account.balance) AND the ability to
validate or compute values. @property gives both, and you can add validation
later without changing code that already uses the attribute.
"""


# --- Example 1: Java-style getter/setter methods (works, but clunky) ---
class ClunkyTemperature:
    def __init__(self, celsius):
        self._celsius = celsius

    def get_celsius(self):
        return self._celsius

    def set_celsius(self, value):
        self._celsius = value


t = ClunkyTemperature(20)
t.set_celsius(25)
print("Example 1:", t.get_celsius())


# --- Example 2: the Pythonic way, @property ---
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius        # goes through the setter, so it is validated

    @property
    def celsius(self):                # getter
        return self._celsius

    @celsius.setter
    def celsius(self, value):         # setter with validation
        if value < -273.15:
            raise ValueError("Below absolute zero is impossible")
        self._celsius = value

    @property
    def fahrenheit(self):             # computed, read-only property
        return self._celsius * 9 / 5 + 32


print("\nExample 2:")
temp = Temperature(25)
print(temp.celsius, temp.fahrenheit)   # 25 77.0
temp.celsius = 100                     # looks like a normal attribute
print(temp.celsius, temp.fahrenheit)   # 100 212.0

print("\nExample 3: validation protects the object")
try:
    temp.celsius = -500
except ValueError as error:
    print("Rejected:", error)
print("Still:", temp.celsius)

print("\nExample 4: read-only property")
try:
    temp.fahrenheit = 50
except AttributeError as error:
    print("AttributeError:", error)


# --- Example 5: practical - Employee with validated salary ---
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self.salary = salary

    @property
    def name(self):                   # no setter -> name cannot be changed
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Salary must be a number")
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value


print("\nExample 5:")
emp = Employee("Asha", 50000)
emp.salary += 5000
print(emp.name, emp.salary)
for bad_value in (-1, "lots"):
    try:
        emp.salary = bad_value
    except (ValueError, TypeError) as error:
        print(f"  {bad_value!r} rejected: {error}")

# --- Example 6: a deleter (optional) ---
print("\nExample 6 (optional): @salary.deleter exists, but is rarely needed.")

# --- Common mistakes ---
print("\nCommon mistakes:")


class Recursive:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value            # store under a DIFFERENT name (_value)

    @value.setter
    def value(self, new_value):
        self._value = new_value       # using self.value here -> infinite recursion


print("  Property 'value' stores data in '_value':", Recursive(3).value)
print("  Don't write properties for everything - plain attributes are fine")
print("  until you need validation or computed values.")
