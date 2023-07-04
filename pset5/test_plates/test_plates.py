from plates import is_valid

# Tests Length
def test_len():
    assert is_valid("OUTATIME") == False
    assert is_valid("H") == False
    assert is_valid("ASSMAN") == True

# Tests Numbers
def test_num():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("50") == False

# Tests Numbers location
def test_mid():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

# Tests Alphanumeric Characters
def test_alnum():
    assert is_valid("PI3.14") == False
    assert is_valid("CS50p") == False