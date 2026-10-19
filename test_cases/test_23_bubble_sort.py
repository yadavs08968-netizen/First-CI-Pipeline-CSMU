import importlib

module = importlib.import_module("23_bubble_sort")
bubble_sort = module.bubble_sort


def test_unsorted_numbers():
    assert bubble_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]


def test_already_sorted():
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]


def test_reverse_sorted():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]


def test_duplicates():
    assert bubble_sort([3, 1, 3, 2]) == [1, 2, 3, 3]


def test_empty_list():
    assert bubble_sort([]) == []


def test_original_list_unchanged():
    numbers = [3, 1, 2]
    bubble_sort(numbers)
    assert numbers == [3, 1, 2]