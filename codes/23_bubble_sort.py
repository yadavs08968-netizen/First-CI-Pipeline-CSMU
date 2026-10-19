"""Program 23: Sort a list using bubble sort."""


def bubble_sort(numbers):
    """Return a new list sorted in ascending order."""
    result = numbers.copy()
    n = len(result)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        if not swapped:
            break

    return result


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Sorted list:", bubble_sort(numbers))