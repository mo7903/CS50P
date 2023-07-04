from seasons import get_birth
from datetime import date
from pytest import raises

def test_date():
    assert get_birth("1999-01-01") == date(1999, 1, 1)
    with raises(SystemExit):
        get_birth("1999-13-50")
    with raises(SystemExit):
        get_birth("September 7, 2003")
