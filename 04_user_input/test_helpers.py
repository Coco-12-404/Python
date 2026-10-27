"""Non-interactive checks for the helpers in examples.py. Run: python test_helpers.py"""

from unittest import mock

from examples import ask_int, ask_yes_no, parse_float, parse_int

assert parse_int(" 42 ") == 42
assert parse_int("4.5") is None
assert parse_int("abc") is None
assert parse_int("") is None
assert parse_float("3.5") == 3.5
assert parse_float("x") is None

# Simulate a user typing a bad value, then a good one
with mock.patch("builtins.input", side_effect=["abc", "", "7"]):
    assert ask_int("n: ") == 7
with mock.patch("builtins.input", side_effect=["maybe", "Y"]):
    assert ask_yes_no("ok?") is True
with mock.patch("builtins.input", side_effect=["NO"]):
    assert ask_yes_no("ok?") is False

print("All input-handling checks passed.")
