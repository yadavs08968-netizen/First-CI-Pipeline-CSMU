import importlib

module = importlib.import_module("24_merge_sorted_lists")
merge_sorted_lists = module.merge_sorted_lists


def test_merge_two_sorted_lists():
    assert merge_sorted_lists([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]


def test_first_list_empty():
    assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]


def test_second_list_empty():
    assert merge_sorted_lists([1, 2, 3], []) == [1, 2, 3]


def test_both_lists_empty():
    assert merge_sorted_lists([], []) == []


def test_duplicate_values():
    assert merge_sorted_lists([1, 2, 2], [2, 3, 3]) == [1, 2, 2, 2, 3, 3]


def test_negative_numbers():
    assert merge_sorted_lists([-5, -1, 3], [-4, 0, 2]) == [-5, -4, -1, 0, 2, 3]


def test_original_lists_unchanged():
    first = [1, 3, 5]
    second = [2, 4]

    merge_sorted_lists(first, second)

    assert first == [1, 3, 5]
    assert second == [2, 4]