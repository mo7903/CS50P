from fuel import convert, gauge
from pytest import raises

def test_convert():
    assert convert("1/2") == 50
    assert convert("1/3") == 33
    assert convert("0/2") == 0
    with raises(ZeroDivisionError):
        convert("1/0")
    with raises(ValueError):
        convert("cat/dog")

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
