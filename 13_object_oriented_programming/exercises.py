"""OOP - practice. Replace each TODO with your own code, then run the file.

Exercises are grouped from beginner to intermediate. Test each one by creating
objects and printing results below your class definitions.
"""

# ---------- Classes, constructors, methods (beginner) ----------

# 1. Create a class `Dog` with __init__(self, name, age) storing both values,
#    and a method `bark()` that returns "<name> says Woof!". Create two dogs.
# TODO

# 2. Create `Rectangle(width, height)` with methods `area()` and `perimeter()`.
# TODO

# 3. Create `BankAccount(owner, balance=0)` with deposit(amount) and
#    withdraw(amount). Reject negative amounts and overdrafts (print or raise
#    ValueError - your choice, but be consistent).
# TODO

# 4. Create `Counter` with increment(), decrement(), reset() and a `value` attribute.
#    Make two counters and show they are independent.
# TODO

# ---------- Class attributes, class and static methods ----------

# 5. Create `Student` with a class attribute `school = "Python High"` and a
#    class attribute that counts how many students were created.
# TODO

# 6. Add a classmethod `from_string("Asha,20")` that builds a Student, and a
#    staticmethod `is_valid_age(age)` that returns True for 5-100.
# TODO

# ---------- Encapsulation and properties ----------

# 7. Create `Thermostat` where the temperature is stored in `_temperature` and
#    exposed through a @property with a setter that only accepts 10-30.
# TODO

# 8. Create `Person` with a read-only `name` property and an `age` property
#    that rejects negative values. Add a computed read-only property `is_adult`.
# TODO

# ---------- Inheritance, overriding, polymorphism ----------

# 9. Create `Vehicle(brand)` with `describe()`. Make `Car` and `Bike` subclasses
#    that override describe(). Use super() in at least one.
# TODO

# 10. Create `Employee(name, salary)` and `Manager(Employee)` with a bonus.
#     Override `annual_pay()` in Manager using super(). Loop over a mixed list.
# TODO

# 11. Create three classes with the same `speak()` method (not related by
#     inheritance). Write a function `make_all_speak(things)` that calls it.
# TODO

# 12. (Multiple inheritance) Create mixins `Swimmer` and `Flyer`, and a `Duck`
#     using both. Print `Duck.__mro__`.
# TODO

# ---------- Abstraction and composition ----------

# 13. Create an abstract class `Shape` (use ABC) with abstract `area()`.
#     Implement `Circle` and `Square`. Show that Shape() raises TypeError.
# TODO

# 14. Build `ShoppingCart` that HAS many `Item(name, price)` objects.
#     Add add_item(), remove_item(name), and total().
# TODO

# ---------- Special methods and identity ----------

# 15. Give your `Item` class __str__ and __repr__. Print one item and a list of items.
# TODO

# 16. Create `Deck` that holds a list of cards and supports len(deck),
#     deck[0], and `card in deck` using __len__, __getitem__, __contains__.
# TODO

# 17. Create `Vector(x, y)` supporting `+`, `==` and a friendly __str__.
# TODO

# 18. Show the difference between `is` and `==` with two equal lists and with
#     two objects of a class that defines __eq__.
# TODO

# ---------- Challenge ----------

# 19. (Challenge) Model a Library: `Library` has many `Book`s; a book can be
#     borrowed or returned; borrowing an unavailable book must be refused.
#     Compare with the finished version in mini_project/ ONLY after trying.
# TODO
