
"""Program 26: Calculate the sum of a list without using sum()."""


def sum_of_list(numbers):
    """Return the total of all numbers in the list."""
    total = 0

    for number in numbers:
        total += number

    return total
