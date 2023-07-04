from working import convert
from pytest import raises

# Tests different hour formats
def test_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

# Tests different hour & min formats
def test_mins():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

# Tests a variety of false input from the user
def test_falsein():
    with raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with raises(ValueError):
        convert("9 AM - 5 PM")
    with raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with raises(ValueError):
        convert("9 to 5")