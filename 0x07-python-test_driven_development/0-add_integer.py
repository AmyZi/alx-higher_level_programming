#!/usr/bin/python3
"""
This is the "add_integer" module.
The 0-add_integer module supplies one function, add_integer(a, b).
"""


def add_integer(a, b=98):
    """Return the addition of two numbers"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b

if __name__ == "__main__":
    # Specify the path to the test file in the 'test' directory.
    test_file = 'test/0-add_integer.txt'

    # Run the doctests from the specified file.
    doctest.testfile(test_file, verbose=True)
