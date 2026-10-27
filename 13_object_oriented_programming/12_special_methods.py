"""Topic 17: Special (dunder) methods.

"Dunder" = double underscore, like __str__. Python calls them automatically
when you use built-in syntax: print(obj), len(obj), a + b, a == b, a < b ...
WHY: they make your objects behave like natural, built-in types.
"""


# --- Example 1: __str__ vs __repr__ ---
class Book:
    def __init__(self, title, author, pages):
        self.title, self.author, self.pages = title, author, pages

    def __str__(self):              # friendly text for users: print(), str(), f-strings
        return f"'{self.title}' by {self.author}"

    def __repr__(self):             # unambiguous text for developers: debugging, lists
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages})"


book = Book("Python Basics", "Asha", 300)
print("Example 1:")
print(book)                # uses __str__
print(repr(book))          # uses __repr__
print([book])              # containers show __repr__

# --- Example 2: __len__, __bool__, and indexing ---
print("\nExample 2:")


class Playlist:
    def __init__(self, songs):
        self.songs = list(songs)

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):             # enables playlist[0] and for-loops
        return self.songs[index]

    def __contains__(self, song):             # enables `song in playlist`
        return song in self.songs


playlist = Playlist(["Intro", "Chorus", "Outro"])
print(len(playlist), playlist[0], "Chorus" in playlist)
for song in playlist:
    print("  -", song)
print("Empty playlist is falsy:", bool(Playlist([])))   # uses __len__


# --- Example 3: operators with __add__, __eq__, __lt__ ---
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented              # let Python raise a clear error
        return Money(self.amount + other.amount)

    def __eq__(self, other):
        return isinstance(other, Money) and self.amount == other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __repr__(self):
        return f"Money({self.amount})"


print("\nExample 3:")
print(Money(50) + Money(25))                    # Money(75)
print(Money(10) == Money(10), Money(10) < Money(20))
print(sorted([Money(30), Money(5), Money(12)])) # sorting uses __lt__
print(max(Money(3), Money(9)))

# --- Example 4: __eq__ and hashing ---
print("\nExample 4:")


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return isinstance(other, Point) and (self.x, self.y) == (other.x, other.y)

    def __hash__(self):                         # needed if objects go in sets/dict keys
        return hash((self.x, self.y))


print(len({Point(1, 2), Point(1, 2), Point(3, 4)}))   # 2 -> equal points collapse

# --- Example 5: __call__ and __enter__ (optional) ---
print("\nExample 5 (optional): __call__ makes objects callable")


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor


triple = Multiplier(3)
print(triple(14))                                 # 42

# --- Common mistakes ---
print("\nCommon mistakes:")


class NoStr:
    pass


print("  Without __str__/__repr__:", NoStr())     # unhelpful <...object at 0x...>
try:
    len(NoStr())
except TypeError as error:
    print("  TypeError:", error)


class EqNoHash:
    def __eq__(self, other):
        return True


try:
    {EqNoHash()}
except TypeError as error:
    print("  Defining __eq__ alone removes hashing:", error)
print("  __str__ must RETURN a string (not print one).")
