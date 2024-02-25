# creating test method main
import pytest


def add_two_numbers(a, b):
    return a + b


# method call -1
def test_small_numbers():
    assert add_two_numbers(10, 12) == 22, "The sum of 10 and 12 should be 22."


# method call -2
def test_big_numbers():
    assert add_two_numbers(100, 300) == 400, "he sum of 100 and 300 should be 400."
