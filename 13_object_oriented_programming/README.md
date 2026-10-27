# 13 - Object-Oriented Programming (OOP)

OOP organizes code around **objects** that bundle data (attributes) with behaviour (methods).
A **class** is the blueprint; an **object** (instance) is something built from it.

```python
class Dog:
    def __init__(self, name):      # constructor
        self.name = name           # instance attribute

    def bark(self):                # instance method
        return f"{self.name} says Woof!"

print(Dog("Rex").bark())
```

## Learning sequence

| File | Topics |
|------|--------|
| `01_classes_and_objects.py` | OOP intro, classes vs objects, defining classes |
| `02_constructor_and_self.py` | `__init__()` and `self` |
| `03_attributes_and_methods.py` | Instance attributes and methods |
| `04_class_attributes_and_methods.py` | Class attributes, `@classmethod`, `@staticmethod` |
| `05_encapsulation.py` | Public / `_protected` / `__name-mangled` conventions |
| `06_properties.py` | Getters, setters, `@property`, validation |
| `07_inheritance.py` | Single, multilevel, multiple inheritance, MRO |
| `08_method_overriding.py` | Overriding and `super()` |
| `09_polymorphism_and_duck_typing.py` | Polymorphism and duck typing |
| `10_abstraction.py` | `abc.ABC` and `@abstractmethod` |
| `11_composition.py` | Composition vs inheritance |
| `12_special_methods.py` | `__str__`, `__repr__`, `__len__`, operators, `__eq__` |
| `13_identity_equality_references.py` | `is` vs `==`, references, copies |
| `mini_project/` | Library Management System |
| `exercises.py` | Practice problems (TODOs only) |

## Key concepts
- **Encapsulation:** keep data with its methods and control how it changes. Python has *no strict private access*; `_name` is a convention and `__name` is name-mangled (renamed to `_Class__name`), not locked.
- **Inheritance:** "is-a" reuse. `super()` calls the parent; the MRO decides which method runs.
- **Polymorphism / duck typing:** different classes, same method name; Python checks what an object can do.
- **Abstraction:** ABCs force subclasses to implement required methods.
- **Composition:** "has-a" reuse; usually more flexible than inheritance.
- **Dunder methods:** make objects work with `print`, `len`, `+`, `==`, sorting.
- **Identity vs equality:** `is` = same object, `==` = equal value.

Optional ideas appear in clearly marked "(optional)" sections (for example `__call__`).

## Run
From the repository root:
```
python 13_object_oriented_programming/01_classes_and_objects.py
python 13_object_oriented_programming/02_constructor_and_self.py
python 13_object_oriented_programming/03_attributes_and_methods.py
python 13_object_oriented_programming/04_class_attributes_and_methods.py
python 13_object_oriented_programming/05_encapsulation.py
python 13_object_oriented_programming/06_properties.py
python 13_object_oriented_programming/07_inheritance.py
python 13_object_oriented_programming/08_method_overriding.py
python 13_object_oriented_programming/09_polymorphism_and_duck_typing.py
python 13_object_oriented_programming/10_abstraction.py
python 13_object_oriented_programming/11_composition.py
python 13_object_oriented_programming/12_special_methods.py
python 13_object_oriented_programming/13_identity_equality_references.py
python 13_object_oriented_programming/exercises.py
```
Mini-project: see [mini_project/README.md](mini_project/README.md).

Some "common mistakes" sections trigger errors on purpose and catch them with `try/except`, so a clean run is expected.
