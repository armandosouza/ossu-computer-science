from numb3rs import validate


def test_numb3rs():
    assert validate('127.0.0.1') == True
    assert validate('512.512.512.512') == False
    assert validate('255.255.255.256') == False
    assert validate('1.1..1.1') == False
    assert validate('2') == False