import secrets
from string import ascii_uppercase, ascii_lowercase, digits, punctuation


def generate_password(size=8):
    """Generates a password with minimum length 8
    Must contain at least one: uppercase, lowercase, number and special character
    """

    if size < 4:
        raise ValueError("Minimum size is 3.")

    chars = (ascii_lowercase + ascii_uppercase + digits + punctuation)

    # Get one of each group of mandatory characters
    lower_char = secrets.choice(ascii_lowercase)
    upper_char = secrets.choice(ascii_uppercase)
    digit_char = secrets.choice(digits)
    special_char = secrets.choice(punctuation)
    password = lower_char + upper_char + digit_char + special_char

    password = password + "".join(secrets.choice(chars) for _ in range(size - 4))

    return password
