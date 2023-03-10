from plates import is_valid


def test_plates():
    assert is_valid("ABCD12") == True
    assert is_valid("000ABC") == False
    assert is_valid("AB12C1") == False
    assert is_valid("1234") == False
    assert is_valid("AB012") == False
    assert is_valid("OUTPUTNOTVALID") == False
    assert is_valid("AB,12") == False