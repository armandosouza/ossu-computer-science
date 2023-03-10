from bank import value


def test_value():
    assert value("hello") == 0
    assert value("how you doing?") == 20
    assert value("what's up?") == 100
    assert value("Hello") == 0