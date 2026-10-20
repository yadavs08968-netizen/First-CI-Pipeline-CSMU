
import importlib
import pytest

module = importlib.import_module("30_decimal_to_binary")
decimal_to_binary = module.decimal_to_binary


def test_convert_zero():
    assert decimal_to_binary(0) == "0"


def test_convert_one():
    assert decimal_to_binary(1) == "1"


def test_convert_positive_number():
    assert decimal_to_binary(10) == "1010"


def test_convert_seven():
    assert decimal_to_binary(7) == "111"


def test_convert_large_number():
    assert decimal_to_binary(255) == "11111111"


def test_negative_number():
    with pytest.raises(ValueError):
        decimal_to_binary(-5)
