import pytest

from ..code.password_generator import generate_password


def test_generate_password():
    password = generate_password()
    assert len(password) == 8
