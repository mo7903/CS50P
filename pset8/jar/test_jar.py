from jar import Jar
from pytest import raises


def test_init():
    jar = Jar(23)
    assert jar.capacity == 23


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(2)
    assert jar.size == 2
    with raises(ValueError):
        jar.deposit(14)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(2)
    assert jar.size == 10
    with raises(ValueError):
        jar.withdraw(14)