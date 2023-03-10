from seasons import convert_to_minutes
from pytest import raises


def test_seasons():
    assert convert_to_minutes("2021-02-24") == "One million, fifty-one thousand, two hundred minutes"


def test_errors():
    with raises(SystemExit):
        convert_to_minutes("ABCD")