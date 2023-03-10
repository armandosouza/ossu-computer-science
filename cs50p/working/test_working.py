from working import convert
import pytest


def test_convert():
    assert convert("12:00 PM to 4:00 PM") == "12:00 to 16:00"
    assert convert("12 PM to 5 PM") == "12:00 to 17:00"


def test_errors():
    with pytest.raises(ValueError):
        convert("2 PM - 5 PM")

    with pytest.raises(ValueError):
        convert("25 AM to 32 PM")