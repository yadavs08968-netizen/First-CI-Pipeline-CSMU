
"""Program 25: Find the maximum and minimum in a list."""


def find_max_min(numbers):
    """Return a tuple containing (maximum, minimum)."""
    if not numbers:
        raise ValueError("The list cannot be empty")

    maximum = numbers[0]
    minimum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number

    return (maximum, minimum)
