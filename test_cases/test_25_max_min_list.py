
import importlib
import pytest

module = importlib.import_module("25_max_min_list")
find_max_min = module.find_max_min


def test_basic_list():
    assert find_max_min([4, 9, 1, 7]) == (9, 1)


def test_single_element():
    assert find_max_min([5]) == (5, 5)


def test_negative_numbers():
    assert find_max_min([-8, -2, -10]) == (-2, -10)


def test_mixed_numbers():
    assert find_max_min([-5, 0, 12, 3]) == (12, -5)


def test_duplicate_values():
    assert find_max_min([4, 4, 4]) == (4, 4)


def test_empty_list_raises_value_error():
    with pytest.raises(ValueError):
        find_max_min([])
