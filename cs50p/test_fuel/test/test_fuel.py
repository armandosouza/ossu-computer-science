from fuel import convert, gauge
import pytest


def test_fuel():
    assert convert("1/2") == 50
    assert convert("1/3") == 33
    assert gauge(1) == "E"
    assert gauge(75) == "75%"
    assert gauge(99) == "F"


def test_errors_fuel():
    with pytest.raises(ZeroDivisionError):
        assert convert("1/0")

    with pytest.raises(ValueError):
        assert convert("cat/dog")