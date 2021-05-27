import unittest

import pytest

from ..code.oop import Dog


# unittest tests
class TestOop(unittest.TestCase):

    def test_feed_dogs(self):
        pass

    def test_are_dogs_hungry(self):
        pass


# pytest tests
def test_feed_dogs():
    pass


def test_are_dogs_hungry():
    pass


# List of Dogs
bobby = Dog('bobby', 10)
dunco = Dog('dunco', 3)
laika = Dog('laika', 6)
my_dogs = [bobby, dunco, laika]
