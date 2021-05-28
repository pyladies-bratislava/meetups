from string import ascii_uppercase, ascii_lowercase, digits, punctuation

import pytest

from ..code.password_generator import generate_password


@pytest.mark.parametrize("size", [n for n in range(0, 20)])
def test_generate_password(size):
    if size < 4:
        with pytest.raises(ValueError):
            generate_password(size=size)
    else:
        password = generate_password(size=size)
        assert len(password) == size

        # Tests if the password has at least one of those character types
        assert any([letter in punctuation for letter in password])
        assert any([letter in digits for letter in password])
        assert any([letter in ascii_lowercase for letter in password])
        assert any([letter in ascii_uppercase for letter in password])

    assert False
