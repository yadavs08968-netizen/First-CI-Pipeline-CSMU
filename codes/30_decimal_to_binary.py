
"""Program 30: Convert a decimal number to binary."""


def decimal_to_binary(number):
    """Convert a non-negative decimal integer to a binary string."""
    if number < 0:
        raise ValueError("Number must be non-negative")

    if number == 0:
        return "0"

    binary = ""

    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2

    return binary
