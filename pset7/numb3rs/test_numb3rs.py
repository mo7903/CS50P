from numb3rs import validate

# Tests different numbers
def test_num():
    assert validate("1.1.1.1") == True
    assert validate("128.168.1.1") == True
    assert validate("512.512.1100.1000") == False
    assert validate("127.299.289.299") == False

# Tests different forms
def test_form():
    assert validate("128.168.1") == False
    assert validate("128.168.1.1.") == False
    assert validate("cat.dog.2.3") == False
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False