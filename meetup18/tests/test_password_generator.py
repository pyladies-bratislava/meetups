import unittest

import pytest

from code.password_generator import generate_password


# unittest tests
class TestGeneratePassword(unittest.TestCase):

    def test_generate_password(self):
        password = generate_password()
        self.assertTrue(len(password) == 8)


# pytest tests
def test_generate_password():
    password = generate_password()
    assert len(password) == 8
