from jar import Jar
from pytest import raises


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert str(jar) == ""

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(1)
    assert str(jar) == "🍪🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪🍪"