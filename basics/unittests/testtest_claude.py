from hello import hello


def test_default():
    assert hello() == "Hello, world"


def test_argument():
    assert hello("Sathwik") == "Hello, Sathwik"

# to run the folder this file (test) is in just by using the folder name as an argument, we need a file __init__.py to be created in the same folder. __init__.py tells python that this file should be treated as a package not just a folder.
