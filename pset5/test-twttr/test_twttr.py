from twttr import shorten

# Tests lowercase input
def test_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("aeiou") == ""

# TESTS UPPERCASE INPUT
def test_upper():
    assert shorten("MacAbotT") == "McbtT"
    assert shorten("AIOUE") == ""

# Tests miscellaneous input
def test_misc():
    assert shorten("arm.1-") == "rm.1-"