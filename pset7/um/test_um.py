from um import count

# Tests the beginning of the sentence
def test_begin():
    assert count("Um, thanks for the album.") == 1
    assert count("um?") == 1
    assert count("hum") == 0

# Tests mid-sentence
def test_mid():
    assert count("Um, thanks, um...") == 2
    assert count("Hello, this tastes yummy") == 0

# Tests miscallaneous input
def test_misc():
    assert count(" ") == 0
    assert count("69") == 0