from bank import value

# Tests 0 values for hello
def test_hello():
    assert value("hello") == 0
    assert value("HeLlo, Newman!") == 0

# Tests 20 values for h-words
def test_h():
    assert value("hi") == 20
    assert value("How You Doin!") == 20

# Tests 100 values for no h-words
def test_none():
    assert value("Sup!") == 100
    assert value("WeeWaa.") == 100