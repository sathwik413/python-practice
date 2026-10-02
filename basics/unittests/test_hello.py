from hello import hello


def test_claude():
    assert hello("Sathwik") == "Hello, Sathwik"
    assert hello() == "Hello, world"


# group the tests seperately
def test_default():
    assert hello() == "Hello, world"


def test_argument():
    assert hello("Sathwik") == "Hello, Sathwik"
