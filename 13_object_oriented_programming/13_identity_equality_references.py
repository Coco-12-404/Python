"""Topic 18: Object identity, equality, and references.

Variables don't hold objects; they REFER to objects.
    ==   asks "do these have equal VALUES?"   (calls __eq__)
    is   asks "are these the SAME object?"    (same identity / memory)
"""

import copy

# --- Example 1: == vs is ---
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print("Example 1:")
print("a == b:", a == b)       # True  - same contents
print("a is b:", a is b)       # False - two separate lists
print("a is c:", a is c)       # True  - c is another name for the same list
print("ids:", id(a) == id(c), id(a) == id(b))


# --- Example 2: for your own classes, == needs __eq__ ---
class Student:
    def __init__(self, student_id, name):
        self.student_id, self.name = student_id, name


class SmartStudent(Student):
    def __eq__(self, other):
        return isinstance(other, SmartStudent) and self.student_id == other.student_id

    def __hash__(self):                 # equal objects must have equal hashes
        return hash(self.student_id)


print("\nExample 2:")
print(Student(1, "Asha") == Student(1, "Asha"))             # False: default is identity
print(SmartStudent(1, "Asha") == SmartStudent(1, "Asha"))   # True: our own rule

# --- Example 3: shared references cause surprises ---
print("\nExample 3:")


class Team:
    def __init__(self, members):
        self.members = members


original_list = ["Asha", "Ravi"]
team_one = Team(original_list)
team_two = Team(original_list)         # both teams share ONE list
team_one.members.append("Meera")
print(team_two.members)                # ['Asha', 'Ravi', 'Meera']  (!)

safe_team = Team(list(original_list))  # copy so the team owns its list
safe_team.members.append("Dev")
print(original_list, safe_team.members)

# --- Example 4: assignment, shallow copy, deep copy ---
print("\nExample 4:")
inner = [1, 2]
original = {"scores": inner}
alias = original                       # same object
shallow = original.copy()              # new dict, SAME inner list
deep = copy.deepcopy(original)         # fully independent
inner.append(3)
print("alias  :", alias["scores"])     # [1, 2, 3]
print("shallow:", shallow["scores"])   # [1, 2, 3]  (shared inner list)
print("deep   :", deep["scores"])      # [1, 2]

# --- Example 5: passing objects to functions ---
print("\nExample 5:")


def add_item(items):
    items.append("new")                # changes the caller's list (same object)


def reassign(items):
    items = ["completely", "different"]   # rebinding a local name only


numbers = ["old"]
add_item(numbers)
reassign(numbers)
print(numbers)                         # ['old', 'new']

# --- Example 6: use `is` for None and singletons ---
print("\nExample 6:")
value = None
print(value is None, value == None)    # prefer `is None`

# --- Common mistakes ---
print("\nCommon mistakes:")
x, y = 1000, 1000
print("  Never use `is` to compare numbers/strings; small-value caching is an")
print("  implementation detail. Use == for values:", x == y)
rows = [[0] * 2] * 3                   # three references to ONE inner list
rows[0][0] = 9
print("  [[0]*2]*3 trap:", rows)
rows_ok = [[0] * 2 for _ in range(3)]
rows_ok[0][0] = 9
print("  list comprehension fix:", rows_ok)
